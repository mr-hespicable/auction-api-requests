import time
import io
import requests
import json
import nbt
import base64

timesLooped = 0
def getInfo(call):
    r = requests.get(call)
    return r.json()
def decode_inventory_data(raw_data):
    data = nbt.nbt.NBTFile(fileobj=io.BytesIO(base64.b64decode(raw_data)))
    extra = data.tags[0].tags[0]['tag']['ExtraAttributes']
    id = extra['id']
    print(id)
#cred. ShadowMobX#0220 on discord
       

USERNAME = input('say username here please\n')
API_KEY = input('say api key here pls\n')
mojang = f"https://api.mojang.com/users/profiles/minecraft/{USERNAME}?"
response = requests.get(mojang)
UUID = response.json()['id']
profile = f"https://api.hypixel.net/player?key={API_KEY}&uuid={UUID}"
PROFILEUUID = profile['player']['stats']['SkyBlock']['profiles']['caccc92b1ecd43998a30901953029379']
print(PROFILEUUID)


auctionsUp = f"https://api.hypixel.net/skyblock/auction?key={API_KEY}&profile={PROFILEUUID}"
auctionResponse = requests.get(auctionsUp)
data = auctionResponse.text
time.sleep(1)

parse_json = json.loads(data)      
auctionList = parse_json['auctions']
for auctionItem in auctionList:
    sold = auctionItem['highest_bid_amount']
    if sold == 0:
        starting_bid = auctionItem['starting_bid'] 
        item_name = auctionItem['item_name']
        print(f'{item_name} costs {starting_bid}. Claimed: {sold}\n')

auctionsSold = f"https://api.hypixel.net/skyblock/auctions_ended?key-{API_KEY}"
soldauctionResponse = requests.get(auctionsSold)
soldData = soldauctionResponse.text
parse_json = json.loads(soldData)
soldauctionList = parse_json['auctions']
time.sleep(1)
    
while True:
    for soldItem in soldauctionList:
        uuid = soldItem['buyer']
        if uuid != '2e82ec5b72354497adfde07170979a72':
            items = 0
            continue
        
        itemCount = 0
        p = itemCount
        itemCount = p+1
        gzipped_data = soldItem['item_bytes']
        item = decode_inventory_data(gzipped_data)
        print(f'Discovered {item} has sold. Profit was ')

    print('starting loop')
    time.sleep(29)
    print('halfway\n')
    time.sleep(29)
    p = timesLooped
    timesLooped = p+1
    if timesLooped == 1:
        print(f'DONE. The program has cycled {timesLooped} time')
    else:
        print(f'DONE. The program has cycled {timesLooped} times')