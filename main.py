import mist_the_rain
import sys
import numpy as np
import pprint

def main():
    # take start location and max radius from user inputs
    start_loc = sys.argv[1]
    radius = sys.argv[2]

    # record api_key for both recreation.gov site and for the openweathermap API
    rec_api_key = "2E3E3762304242879ADF063FF3239815"
    url = "https://ridb.recreation.gov/api/v1/facilities"
    owm_api_key = '201d8d3928b5f416ea976faa570d99c2'


    # take input location and convert to gps
    start_lat, start_lon = mist_the_rain.get_gps(start_loc)

    # get a list of locations within the certain range of location
    output_data = mist_the_rain.get_facilities(start_lat, start_lon, radius, rec_api_key, url)
    output_data = mist_the_rain.weather_dict(output_data, owm_api_key)
    np.save('output.npy', output_data)
    pprint.pprint(output_data)


if __name__ == '__main__':
    main()
