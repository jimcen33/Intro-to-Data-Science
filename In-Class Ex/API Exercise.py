import json
import requests
import pprint

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    
    #Get the top artist from last.fm geo.getTopArtist API
    data=requests.get(url).text
    
    #Transfer the json object in to Python-like dictionary
    data=json.loads(data)
    
    #Use pprint to check out the json structure to find the artist name
    #pprint.pprint(data['topartists']['artist'][0])
    
    return  data['topartists']['artist'][0]['name'] # return the top artist in Spain

