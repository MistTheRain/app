'''
This file contains all the functions used to determine weather and distance from a given location
'''

import requests
import json
import urllib2
from geopy.geocoders import Nominatim
import distance


def get_facilities(latitude, longitude, radius,api_key,url):
    ''' Finds all facilities offering hiking or climbing in a radius mile radius of the coordinates.
    returns their name, latitude, and longitude, sorted by distance from the starting point.'''

    offset = 0
    params = {"latitude": latitude, "longitude":longitude, "apikey": api_key, "radius":radius, "activity":[14], "full":"compact", "offset":offset}

    r = requests.get(url, params=params)
    text = r.text
    data = json.loads(text)
    max_records = data['METADATA']['RESULTS']['TOTAL_COUNT']
    data = data['RECDATA']
    output_data = []
    for facility in data:
        output_data.append({'name':facility['FacilityName'], 'latitude':facility['FacilityLatitude'], 'longitude':facility['FacilityLongitude'],
                            'distance': distance.distance(longitude, facility["FacilityLongitude"], latitude, facility["FacilityLatitude"])})

    while offset<max_records:
        offset += 50
        params = {"latitude": latitude, "longitude":longitude, "apikey": api_key, "radius":radius, "activity":[14], "full":"compact", "offset":offset}
        r = requests.get(url, params=params)
        text = r.text
        data = json.loads(text)
        data = data['RECDATA']
    for facility in data:
        output_data.append({'name': facility['FacilityName'],
                            'latitude': facility['FacilityLatitude'],
                            'longitude': facility['FacilityLongitude'],
                            'distance': distance.distance(longitude, facility["FacilityLongitude"], latitude, facility["FacilityLatitude"])})


    output_data.sort(key=lambda facility: facility['distance'])

    return output_data


def find_weather(lat, lon, api_key):
    # url for API query
    url = 'http://api.openweathermap.org/data/2.5/' \
           'forecast?lat={0}&lon={1}&APPID={2}&units=imperial'.format(lat, lon, api_key)
    data = json.load(urllib2.urlopen(url))

    # only grab the first
    pred = data['list'][0]

    # features that we want to grab from this data set
    description = pred['weather'][0]['description']
    icon_id = pred['weather'][0]['icon']  # use this to get the image for website of weather
    temp = pred['main']['temp']
    max_temp = pred['main']['temp_max']
    min_temp = pred['main']['temp_min']
    wind = pred['wind']
    humidity = pred['main']['humidity']

    return description, icon_id, temp, max_temp, min_temp, wind, humidity


def get_gps(start_loc):

    geolocator = Nominatim()
    location1 = geolocator.geocode(start_loc)

    return location1.latitude, location1.longitude