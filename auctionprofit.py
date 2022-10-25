import gzip
import time
import io
import requests
import json
import nbt
import base64


def getInfo(call):
    r = requests.get(call)
    return r.json
def decode_inventory_data(raw_data):
       data = nbt.nbt.NBTFile(fileobj = io.BytesIO(base64.b64decode(raw_data)))
       extra = data.tags[0].tags[0].__getitem__('tag').__getitem__('ExtraAttributes')
       id = extra.__getitem__('id')
       print(id)
               
       
while True:
    USERNAME = 'websafe'
    API_KEY = "4c24c4b5-ad52-4bb9-ac0e-d506a1a8793a"
    mojang = f"https://api.mojang.com/users/profiles/minecraft/{USERNAME}?"
    response = requests.get(mojang)
    UUID = response.json()['id']
    PROFILEUUID = "caccc92b1ecd43998a30901953029379"


    auctionsUp = f"https://api.hypixel.net/skyblock/auction?key={API_KEY}&profile={PROFILEUUID}"
    auctionResponse = requests.get(auctionsUp)
    data = auctionResponse.text


    x = 1

    time.sleep(1)
    parse_json = json.loads(data)

    n = 0        
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
    
    
        
    for soldItem in soldauctionList:
        uuid = soldItem['buyer']
        if uuid == '2e82ec5b72354497adfde07170979a72':
            gzipped_data = soldItem['item_bytes']
            decode_inventory_data(gzipped_data)
            exit()
            
            
        else:
            print('No matching auctions found.')
    time.sleep(15)
    print('halfway')
    time.sleep(15)  