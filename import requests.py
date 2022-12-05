 
import requests

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'steam://rungameid/837380'

r = requests.get(url, headers=headers)
#print(r.content)

with open('sec_bhavdata_full.csv', 'wb') as fh:
    fh.write(r.content)
