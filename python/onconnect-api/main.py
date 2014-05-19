from constants.config import onconnect_apikey
from datetime import date
import requests


zipcode = '10013'
radius = '30'
startdate = str(date.today())
url = 'http://data.tmsapi.com/v1/movies/showings?startDate=' + startdate + '&zip=' + zipcode + '&radius=' + radius + '&api_key=' + onconnect_apikey
response = requests.get(url)


with open('data/movies_playing' + str(date.today()) + '.json', 'wb') as f:
    f.write(response.text.encode('utf-8'))
