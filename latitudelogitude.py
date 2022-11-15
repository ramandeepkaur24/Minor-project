import requests
import json

send_url = "http://api.ipstack.com/check?access_key=6cd7ed70-6013-11ed-92c8-5d8618b22bee"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']