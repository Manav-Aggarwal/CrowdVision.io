import cv2
import time
import urllib3
from is_military import predict
from is_military_resnet import *
from send_data import ping_server, get_location


def cv_to_pil_img(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return Image.fromarray(img)


cv2.namedWindow("webcam")
vc = cv2.VideoCapture(1)

net = cv2.dnn.readNetFromCaffe('models/bvlc_googlenet.prototxt', 'models/bvlc_googlenet.caffemodel')
rows = open('synset_words.txt').read().strip().split("\n")
classes = [r[r.find(" ") + 1:].split(",")[0] for r in rows]

time.sleep(2)

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

begin = time.time()
http = urllib3.PoolManager()
path = 'locations.txt'
while rval:
    print("step:", (time.time() - begin))
    cv2.imshow("webcam", frame)
    rval, frame = vc.read()

    (h, w) = frame.shape[:2]
    # calculate the center of the image
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    frame = cv2.warpAffine(frame, M, (h, w))
    wasFound = predict(frame, net, classes)
    if wasFound:
        with open(path, 'a') as f:
            f.write(str(get_location()) + "\n")
        time.sleep(3)
    key = cv2.waitKey(20)
    if key == 27:
        break
cv2.destroyWindow("webcam")