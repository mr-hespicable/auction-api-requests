

import requests

data = requests.get('https://api.hypixel.net/skyblock/bazaar').json()

products = data['products']
inkSac = products['INK_SAC']
print(inkSac['quick_status']['buyPrice'])

