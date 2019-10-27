import requests 
  
# defining the api-endpoint  
API_ENDPOINT = "http://pastebin.com/api/api_post.php"
  
# your API key here 
API_KEY = "XXXXXXXXXXXXXXXXX"
  
# your source code here 
source_code = ''' 
print("Hello, world!") 
a = 1 
b = 2 
print(a + b) 
'''
  
# data to be sent to api 
data = {'api_dev_key':API_KEY, 
        'api_option':'paste', 
        'api_paste_code':source_code, 
        'api_paste_format':'python'} 
  
# sending post request and saving response as response object 


def get_location():
	ip_request = requests.get('https://get.geojs.io/v1/ip.json')
	my_ip = ip_request.json()['ip']
	geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
	geo_request = requests.get(geo_request_url)
	geo_data = geo_request.json()
	return location
	
def ping_server():
	currLocation = get_location()
	r = http.request('POST', API_ENDPOINT,
                 headers = {'Content-Type': 'application/json'},
                 body = currLocation)
	# extracting response text  
	return r