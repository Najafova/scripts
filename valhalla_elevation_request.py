# This script receives file path, latitude and longitutde as input, makes request to Valhalla Routing Engine Demo Server and outputs received elevation 

import sys
import requests

# URL of OSM elevation endpoint
VALHALLA_URL = "https://valhalla1.openstreetmap.de/height?height_precision=2"

# Print received arguments
print('Argument List: ' + str(sys.argv))
# Extract latitude and longitude
file_path = sys.argv[1]
lat = sys.argv[2]
lon = sys.argv[3]
print('Latitude = ' + lat + ', longitude = ' + lon)

# Sending a request and reading response
request_body = '{"range":false,"shape":[{"lat":' + str(lat) + ',"lon":' + str(lon) + '}]}'
print('Sending POST ' + request_body + ' to url ' + VALHALLA_URL)
response = requests.post(VALHALLA_URL, request_body)
print('Received response with code ' + str(response.status_code))
results = response.json()["height"]
elevation = results[0]

# Print and output received elevation
print('Received elevation: ' + str(elevation))
with open(file_path, 'w') as f:
    f.write(str(elevation) + '\n')