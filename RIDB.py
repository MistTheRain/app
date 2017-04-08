import requests
import json
import distance

def get_facilities(latitude, longitude, radius, MAXRADIUS,api_key,url):
    ''' Finds all facilities offering hiking or climbing in a radius mile radius of the coordinates.
    returns their name, latitude, and longitude, sorted by distance from the starting point.'''
    radius = min(radius, MAXRADIUS)
    print('test1')
    offset = 0
    params = {"latitude": latitude, "longitude":longitude, "apikey": api_key, "radius":radius, "activity":[14], "full":"compact", "offset":offset}

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

    print('test2')
    return output_data

def main():

    api_key = "2E3E3762304242879ADF063FF3239815"
    url = "https://ridb.recreation.gov/api/v1/facilities"
    MAXRADIUS = 200
    latitude = 34.0122
    longitude = -116.168
    radius = 100

    output_data = get_facilities(latitude, longitude, radius, MAXRADIUS,api_key,url)

if __name__ == '__main__':
    main()