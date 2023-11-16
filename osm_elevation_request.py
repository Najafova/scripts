# This script receives file path, latitude and longitutde as input, makes request to OSM Open Elevation Server and outputs received elevation 

import sys
import requests

# URL of OSM elevation endpoint
OSM_URL = "https://api.open-elevation.com/api/v1/lookup?locations={lat},{lon}"

# Print received arguments
print('Argument List: ' + str(sys.argv))
# Extract latitude and longitude
file_path = sys.argv[1]
lat = sys.argv[2]
lon = sys.argv[3]
print('Latitude = ' + lat + ', longitude = ' + lon)

# Forming URL
url = OSM_URL.format(lat = lat, lon = lon)
print('Sending GET to url ' + url)

# Sending a request and reading response
response = requests.get(url)
print('Received response with code ' + str(response.status_code))
results = response.json()["results"]
elevation = results[0]["elevation"]

# Print and output received elevation
print('Received elevation: ' + str(elevation))
with open(file_path, 'w') as f:
    f.write(str(elevation) + '\n')