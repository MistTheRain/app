import json
import urllib2


def find_weather(lat, lon, api_key):
    # url for API query
    url = 'http://api.openweathermap.org/data/2.5/' \
           'forecast?lat={0}&lon={1}&APPID={2}&units=imperial'.format(lat, lon, api_key)
    data = json.load(urllib2.urlopen(url))

    # only grab the first
    pred = data['list'][0]

    # features that we want to grab from this data set
    description = pred['weather'][0]['description']
    descript_id = pred['weather'][0]['id']  # use this to get the image for website of weather
    temp = pred['main']['temp']
    max_temp = pred['main']['temp_max']
    min_temp = pred['main']['temp_min']
    wind = pred['wind']
    humidity = pred['main']['humidity']

    return description, descript_id, temp, max_temp, min_temp, wind, humidity

def main():
    # lat/lon for testing
    lat = 36.13129
    lon = -115.42453
    #  openweathermap api key
    api_key = '201d8d3928b5f416ea976faa570d99c2'

    description, descript_id, temp, max_temp, min_temp, wind, humidity = find_weather(lat, lon,
                                                                                      api_key)


if __name__ == '__main__':
    main()