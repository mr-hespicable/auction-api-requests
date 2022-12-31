import time, io, requests, os, nbt, base64

#thanks to ShadowMobX#0220 for refining this function. give him an internship
debugMode = 0
USERNAME = input('paste username here\n')
API_KEY = input('paste api key here\n')
def checkProfile():
    global PREFERRED_PROFILE
    PREFERRED_PROFILE = input('paste name of active profile here\n')
    profile_name_list = ['Apple','Banana','Blueberry','Coconut','Cucumber','Grapes','Kiwi','Lemon','Lime','Mango','Orange','Papaya','Pear','Peach','Pineapple','Pomegranate','Raspberry','Strawberry','Tomato','Watermelon','Zucchini']
    if PREFERRED_PROFILE not in profile_name_list:
        print('Not a valid profile: try again.')
        checkProfile()
    return PREFERRED_PROFILE
checkProfile()


def response(call):
    r = requests.get(call)
    return r.json()

def prettify(string):
    return ('{:,}'.format(string))

def countdown(t):
    while t>= 10:
        print(t, end='\r')
        t -= 1
        time.sleep(1)
    print('  ', end='\r')
    while t >= 0:
        print(t, end='\r')
        t -= 1
        time.sleep(1)
        
class getInf:
    def getProfileID(self): #returns the profile ID of the player
        self.uuid = response(f'https://api.mojang.com/users/profiles/minecraft/{USERNAME}')['id'] #uuid of the player
        for profile in response(f'https://api.hypixel.net/player?key={API_KEY}&uuid={self.uuid}')['player']['stats']['SkyBlock']['profiles']:
            profileName = response(f'https://api.hypixel.net/player?key={API_KEY}&uuid={self.uuid}')['player']['stats']['SkyBlock']['profiles'][profile]['cute_name'] #skyblock profile name of the player
            if profileName == PREFERRED_PROFILE:
                profileID = response(f'https://api.hypixel.net/player?key={API_KEY}&uuid={self.uuid}')['player']['stats']['SkyBlock']['profiles'][profile]['profile_id']
                if debugMode == 1:
                    url = f'https://api.hypixel.net/player?key={API_KEY}&uuid={self.uuid}'
                    print(f'profile URL is {url}')
                return profileID #skyblock profile id of the player
            else:
                continue
    
    def getPresentAuctions(self): #returns the player's auctions that are/were up on the auction house
        return response(f'https://api.hypixel.net/skyblock/auction?key={API_KEY}&profile={z.getProfileID()}')['auctions']
    
    def getAuctionUID(self,url): #returns the UID of an auction
        return response(url)['nbtData']['data']['uid']
    
    def getPastSales(self,uid): #returns the past sales of an auction, given the UID
        url = f'https://sky.coflnet.com/api/auctions/uid/{uid}/sold'
        if debugMode == 1:
            print(f'url for past sales is {url}')
        return response(f'https://sky.coflnet.com/api/auctions/uid/{uid}/sold')

    def getPastAuctionInfo(self,past):
        url = f'https://sky.coflnet.com/api/auction/{past}'
        if debugMode == 1:
            print(f'url for past sales is {url}')
        return response(f'https://sky.coflnet.com/api/auction/{past}')

    def getAuctionsSold(self,itemID):
        url = f'https://sky.coflnet.com/api/auctions/tag/{itemID}/sold?page=1&pageSize=200'
        if debugMode == 1:
            print(f'url for sold auction list is {url}')
        return response(f'https://sky.coflnet.com/api/auctions/tag/{itemID}/sold?page=1&pageSize=200')
z = getInf()

class getEncoded:
    def data(raw_data):
        return nbt.nbt.NBTFile(fileobj=io.BytesIO(base64.b64decode(raw_data)))
    def id(nbt_data):
        extra = nbt_data.tags[0].tags[0]['tag']['ExtraAttributes']
        return extra['id']
    
    def name(nbt_data):
        z = nbt_data.tags[0].tags[0]['tag']['ExtraAttributes']
        if str(z['id']) == 'PET':
            petName = response(str(z['petInfo']))['type']
            return petName
            
profitList = []
priceList = []

url = f'https://api.hypixel.net/skyblock/auction?key={API_KEY}&profile={z.getProfileID()}'
if debugMode == 1:
    print(f'url for auctions on AH is {url}')

while True:
    for auctionItem in z.getPresentAuctions(): #finding price of item
        sold = auctionItem['highest_bid_amount']
        if sold == 0:
            starting_bid = auctionItem['starting_bid']
            itemName = auctionItem['item_name']
            print(f'Checking {itemName}...')
            item_bytes = auctionItem['item_bytes']['data']
            nbt_data = getEncoded.data(item_bytes)
            auctionID = getEncoded.id(nbt_data)
            auctionNameID = getEncoded.name(nbt_data)
            if auctionID == 'PET':
                itemID = f'PET_{auctionNameID}'
            else:
                itemID = auctionID
            
            auctionUUID = auctionItem['uuid']
            
            if debugMode == 1:
                xzy = f'https://sky.coflnet.com/api/auction/{auctionUUID}'
                print(f'url for UID of auction is {xzy}')
            auctionUid = z.getAuctionUID(f'https://sky.coflnet.com/api/auction/{auctionUUID}/')
            auctionPastSales = z.getPastSales(auctionUid)
            if auctionPastSales != []:    
                for sale in auctionPastSales:
                    if sale['buyer'] == z.uuid:
                        boughtAuctionInfo = z.getPastSales(sale['uuid'])
                        boughtAuctionRawPrice = boughtAuctionInfo['bids'][0]['amount']
            else:
                continue
            auctionsSold = z.getAuctionsSold(itemID)
            
            for soldItem in auctionsSold:
                uuid = soldItem['auctioneerId']
                price = soldItem['highestBidAmount']
            profit = (starting_bid - boughtAuctionRawPrice)*0.99
            profitList.append(str(profit))
            priceList.append(str(boughtAuctionRawPrice))
            print(f'Bought {itemName} for {prettify(boughtAuctionRawPrice)} and selling {itemName} for {prettify(starting_bid)}, making {prettify(profit)}.\n')
    totalProfit = sum([float(x) for x in profitList])
    totalCost = sum([float(y) for y in priceList])
    if totalCost == 0:
        totalCost = 1
    if totalProfit != 0:
        print(f'The total amount of profit you will make is {prettify(totalProfit)} ({prettify(round(float(100*(totalProfit/totalCost))))}%). You spent {prettify(totalCost)}')
    else:
        print(f'No items were found to have been flipped for a profit.')
    countdown(30)
    os.system('clear')