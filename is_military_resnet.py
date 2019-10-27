"""
created by: Donghyeon Won
"""

from __future__ import print_function
import os
import argparse
import numpy as np
import pandas as pd
import time
import shutil
from PIL import Image
from tqdm import tqdm

import torch
from torch.utils.data import Dataset, DataLoader
from torch.autograd import Variable
import torchvision.models as models
import torchvision.transforms as transforms

from util import pil_loader, modified_resnet50, ProtestDatasetEval, ProtestDatasetEvalSingle


#python3 pred.py --img_path /Users/Manav/Downloads/CalHacks6/protest-detection-violence-estimation/imgs/police-200.jpg --output_csvpath result.csv --model model_best.pth.tar

def eval_one_img(img, model):
        """
        return model output of all the images in a directory
        """
        model.eval()
        num_workers = 4
        batch_size = 16
        dataset = ProtestDatasetEvalSingle(img = img)
        data_loader = DataLoader(dataset,
                                num_workers = num_workers,
                                batch_size = batch_size)

        outputs = []
        for i, sample in enumerate(data_loader):
            imgpath, input = sample['imgpath'], sample['image']
            input_var = Variable(input)
            output = model(input_var)
            outputs.append(output.cpu().data.numpy())

        df = pd.DataFrame(np.zeros((1, 12)))
        df.columns = ["protest", "violence", "sign", "photo",
                      "fire", "police", "children", "group_20", "group_100",
                      "flag", "night", "shouting"]
        df.iloc[:,:] = np.concatenate(outputs)
        return df

def main():

    # load trained model
    print("*** loading model from {model}".format(model = args.model))
    model = modified_resnet50()
    if args.cuda:
        model = model.cuda()
    model.load_state_dict(torch.load(args.model, map_location='cpu')['state_dict'])
    print("*** calculating the model output of the images in {img_dir}"
            .format(img_dir = args.img_path))
   
    #df = eval_one_dir('/Users/Manav/Downloads/CalHacks6/protest-detection-violence-estimation/new_imgs', model)
    img = pil_loader(args.img_path)
    df = eval_one_img(img, model)
    # write csv file
    
    #df.to_csv(args.output_csvpath, index = False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--img_path",
                        type=str,
                        required = True,
                        help = "image path to calculate output of"                        )
    parser.add_argument("--output_csvpath",
                        type=str,
                        default = "result.csv",
                        help = "path to output csv file"
                        )
    parser.add_argument("--model",
                        type=str,
                        required = True,
                        help = "model path"
                        )
    parser.add_argument("--cuda",
                        action = "store_true",
                        help = "use cuda?",
                        )
    parser.add_argument("--workers",
                        type = int,
                        default = 4,
                        help = "number of workers",
                        )
    parser.add_argument("--batch_size",
                        type = int,
                        default = 16,
                        help = "batch size",
                        )
    args = parser.parse_args()

    main()
