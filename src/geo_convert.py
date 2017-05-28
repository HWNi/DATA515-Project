import geocoder
import pandas
import numpy


def geo_forward(address):
    """
    A function using the Geocoding.
    Using the the Bing map API key converts the given address or location
    into latitude and longitude.

    Parameter: address

    Return: latitude and longitude corresponding to this address
    """
    api_key = "Ao_MmbLy7h-iF1O6foR3V615c0sU5M-mgYaSDYoZGoy9_9xhnCj-7Ws4tuY5FDvV"
    g = geocoder.bing(address, key=api_key)
    latitude = g.lat
    longitude = g.lng
    return latitude, longitude

def geo_reverse(latitude, longitude):
    """
    A function using the Reverse Geocoding.
    Using the the Bing map API key converts the given latitude and longitude to
    a phyiscal address or location.

    Parameters: latitude and longitude.

    Return: a zipcode corresponding to the latitude and longitude pair.
    """
    api_key = "Ao_MmbLy7h-iF1O6foR3V615c0sU5M-mgYaSDYoZGoy9_9xhnCj-7Ws4tuY5FDvV"
    g = geocoder.bing([latitude, longitude], method="reverse", key=api_key)
    zipcode = g.postal
    return zipcode
