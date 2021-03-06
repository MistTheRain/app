from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    lat, long = main()
    return "Hello World! %s %s" % (lat, long)
	
	

	
# location-input transformation
# address-input -> latitude/longitude coordinates

from geopy.geocoders import Nominatim
import math
import requests
import json
import distance


# finding nearby trails

def get_facilities(latitude, longitude, radius, MAXRADIUS,api_key,url):

    ''' Finds all facilities offering hiking or climbing in a radius mile radius of the coordinates.
    returns their name, latitude, and longitude, sorted by distance from the starting point.'''
    radius = min(radius, MAXRADIUS)
    offset = 0
    params = {"latitude" : latitude, "longitude":longitude, "apikey": api_key, "radius":radius, "activity":[14], "full":"compact", "offset":offset}

    r = requests.get(url, params=params)
    text = r.text
    data = json.loads(text)
    max_records = data['METADATA']['RESULTS']['TOTAL_COUNT']
    data = data['RECDATA']
    output_data = []
    for facility in data:
        output_data.append({'name':facility['FacilityName'], 'latitude':facility['FacilityLatitude'], 'longitude':facility['FacilityLongitude']})

    while offset<max_records:
        offset += 50
        params = {"latitude": latitude, "longitude":longitude, "apikey": api_key, "radius":radius, "activity":[14], "full":"compact", "offset":offset}
        r = requests.get(url, params=params)
        text = r.text
        data = json.loads(text)
        data = data['RECDATA']
        for facility in data:
            output_data.append({'name':facility['FacilityName'], 'latitude':facility['FacilityLatitude'], 'longitude':facility['FacilityLongitude']})

        output_data.sort(key=lambda facility: distance.distance(longitude, facility["longitude"], latitude, facility["latitude"]))

    return output_data


def main():

    api_key = "2E3E3762304242879ADF063FF3239815"
    url = "https://ridb.recreation.gov/api/v1/facilities"
    MAXRADIUS = 200
    radius = 100

    #input location
    geolocator = Nominatim()
    location1 = geolocator.geocode("Northwestern University, Evanston, IL")
    coordinates1 = (location1.latitude, location1.latitude)

    #output location
    output_data = get_facilities(location1.latitude, location1.longitude, radius, MAXRADIUS,api_key,url)
    location2_latitude = output_data[0]['latitude']
    location2_longitude = output_data[0]['longitude']

    print output_data[0]['name']
    print location2_latitude
    print location2_longitude

    # distance btwn locations
    print distance.distance(location1.longitude, location2_longitude, location1.latitude, location2_latitude)

    return location2_latitude, location2_longitude
    
    
if __name__ == "__main__":
    app.run()