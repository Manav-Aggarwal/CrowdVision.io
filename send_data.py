import requests 
  
# defining the api-endpoint  
API_ENDPOINT = "http://pastebin.com/api/api_post.php"
  
# sending post request and saving response as response object 


def get_location():
	ip_request = requests.get('https://get.geojs.io/v1/ip.json')
	my_ip = ip_request.json()['ip']
	geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
	geo_request = requests.get(geo_request_url)
	geo_data = geo_request.json()
	return geo_data
	
def ping_server():
	currLocation = get_location()
	r = http.request('POST', API_ENDPOINT,
                 headers = {'Content-Type': 'application/json'},
                 body = currLocation)
	# extracting response text  
	return r