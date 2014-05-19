import requests
from constants.config import MEDIA_ID, AFF_ID

lat = '40.7127'
lng = '-74.0059'
limit = 50
offset = 0


def makeURL(lat, lng, limit, offset):
    url = 'https://partner-api.groupon.com/deals.json?tsToken=US_AFF_0_' + AFF_ID + '_' + MEDIA_ID + '_0&lat=' + lat + '&lng=' + lng + '&offset=' + str(offset) + '&limit=' + str(limit)
    return url

# fetch 500 records
for i in range(0, 10):
    URL = makeURL(lat, lng, limit, offset)
    response = requests.get(URL)
    with open('data/groupon' + str(i) + '.json', 'wb') as f:
        f.write(response.text.encode('utf-8'))
    offset += limit
