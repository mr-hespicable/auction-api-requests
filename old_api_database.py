import io, requests, os, nbt, base64, re

#thanks to ShadowMobX#0220 for refining this function. give him an internship


def response(call):
    r = requests.get(call)
    return r.json()

def prettify(string):
    return ('{:,}'.format(string))

profile_name_list = []
def checkProfile():
    profiles = response(f'https://sky.shiiyu.moe/api/v2/profile/{USERNAME}')['profiles']
    for profile in profiles:
        if profiles[profile]['current'] == False:
            continue
        elif profiles[profile]['current'] == True:
            return profiles[profile]['cute_name']

def getProfileID(username, api_key): #returns the profile ID of the player
    uuid = response(f'https://api.mojang.com/users/profiles/minecraft/{username}')['id'] #uuid of the player
    for profile in response(f'https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}')['player']['stats']['SkyBlock']['profiles']:
        profileName = response(f'https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}')['player']['stats']['SkyBlock']['profiles'][profile]['cute_name'] #skyblock profile name of the player
        if profileName == checkProfile():
            profileID = response(f'https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}')['player']['stats']['SkyBlock']['profiles'][profile]['profile_id']
            return profileID #skyblock profile id of the player
        else:
            continue

def getPresentAuctions(): #returns the player's auctions that are/were up on the auction house
    return response(f'https://api.hypixel.net/skyblock/auction?key={API_KEY}&profile={getProfileID(USERNAME, API_KEY)}')['auctions']

def getAuctionUID(url): #returns the UID of an auction
    return response(url)['nbtData']['data']['uid']

def getPastSales(uid): #returns the past sales of an auction, given the UID
    url = f'https://sky.coflnet.com/api/auctions/uid/{uid}/sold'
    return response(f'https://sky.coflnet.com/api/auctions/uid/{uid}/sold')

def getPastAuctionInfo(past):
    url = f'https://sky.coflnet.com/api/auction/{past}'
    return response(f'https://sky.coflnet.com/api/auction/{past}')

def getAuctionsSold(itemID):
    url = f'https://sky.coflnet.com/api/auctions/tag/{itemID}/sold?page=1&pageSize=200'
    return response(f'https://sky.coflnet.com/api/auctions/tag/{itemID}/sold?page=1&pageSize=200')

def data(raw_data):
    return nbt.nbt.NBTFile(fileobj=io.BytesIO(base64.b64decode(raw_data)))
def id(nbt_data):
    extra = nbt_data.tags[0].tags[0]['tag']['ExtraAttributes']
    return extra['id']

def name(nbt_data):
    z = nbt_data.tags[0].tags[0]['tag']['ExtraAttributes']
    if str(z['id']) == 'PET':
        pet_string = str(z['petInfo'])
        z = str(re.search("\".*\"", str(re.search(":\".*\",", str(re.search("\"type\":\".*\",\"a", pet_string))))).group()).replace('\"', '')
        return f'PET_{z}'
            

USERNAME = 'websafe'#input('paste username here\n')
API_KEY = '6fa96f15-a6bd-40cc-b9fa-c518d30deb79'#input('paste api key here\n')
UUID = response(f'https://api.mojang.com/users/profiles/minecraft/{USERNAME}')['id']

while True:
    profitList = []
    priceList = []
    for auctionItem in getPresentAuctions(): #finding price of item
        sold = auctionItem['highest_bid_amount']
        if sold == 0:
            starting_bid = auctionItem['starting_bid']
            itemName = auctionItem['item_name']
            item_bytes = auctionItem['item_bytes']['data']
            nbt_data = data(item_bytes)
            auctionID = id(nbt_data)
            auctionNameID = name(nbt_data)
            if auctionID == 'PET':
                itemID = f'PET_{auctionNameID}'
            else:
                itemID = auctionID

            auctionUUID = auctionItem['uuid']

            auctionUid = getAuctionUID(f'https://sky.coflnet.com/api/auction/{auctionUUID}/')
            auctionPastSales = getPastSales(auctionUid)

            if auctionPastSales != []:    
                for sale in auctionPastSales:
                    if sale['buyer'] == UUID and len(auctionPastSales) > 1:
                        boughtAuctionInfo = getPastAuctionInfo(sale['uuid'])['bids']
                        boughtAuctionRawPrice = boughtAuctionInfo[0]['amount']
                    else:
                        boughtAuctionRawPrice = 0
            auctionsSold = getAuctionsSold(itemID)

            for soldItem in auctionsSold:
                uuid = soldItem['auctioneerId']
                price = soldItem['highestBidAmount']
            profit = (starting_bid - boughtAuctionRawPrice)*0.99
            profitList.append(str(profit))
            priceList.append(str(boughtAuctionRawPrice))
            totalProfit = prettify(round(int(sum([float(x) for x in profitList]))))
            totalCost = prettify(int(sum([float(y) for y in priceList])))
    print(f"""
          TOTAL PROFIT IN AUCTION HOUSE: {totalProfit}
          TOTAL AMOUNT SPENT ON ALL ITEMS IN AUCTION HOUSE: {totalCost}
          """)
    exit()