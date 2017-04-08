
# location-imput transformation
# address-imput -> latitude/longitude coordinates

from geopy.geocoders import Nominatim
geolocator = Nominatim()
location1 = geolocator.geocode ("Northwestern University, Evanston, IL")
imput_location1 = (location1.latitude, location1.longitude)

"""a second location... will eventually need to be found through searching a database of parks..."""
location2 = geolocator.geocode ("Starved Rock, IL")
imput_location2 = (location2.latitude, location2.longitude)

# distance between locations 1 and 2
# coordinates of locations 1 + 2 -> distance between two coordinates in miles

from geopy.distance import great_circle
print (great_circle(imput_location1, imput_location2).miles)



