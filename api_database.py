import io, requests, os, nbt, base64



def _response(call):
    r = requests.get(call)
    return r.json()
def __ProfileStats(uuid):
    url = f'https://sky.shiiyu.moe/api/v2/profile/{uuid}'
    profiles = _response(url)['profiles']
    for profile in profiles:
        profile_id = profiles[profile]['profile_id']
        cute_name = profiles[profile]['cute_name']
        current = profiles[profile]['current']
        if current == True:
            return cute_name, profile_id
        else:
            continue

def ProfileName(uuid):
    'Returns the name of the profile, given a uuid.'
    return __ProfileStats(uuid)[0]
def ProfileID(uuid):
    'Returns the id of the profile, given a uuid.'
    return __ProfileStats(uuid)[1]

def __decode(raw_data):
    return nbt.nbt.NBTFile(fileobj=io.BytesIO(base64.b64decode(raw_data)))
def __id(nbt_data):
    extra = nbt_data.tags[0].tags[0]['tag']['ExtraAttributes']
    return extra['id']
def __name(nbt_data):
    z = nbt_data.tags[0].tags[0]['tag']['ExtraAttributes']
    if str(z['id']) == 'PET':
        petName = _response(str(z['petInfo']))['type']
        return petName

class get:   
    def uuid(username):
        "Returns the name and uuid of the player, given a username."
        url = f'https://api.mojang.com/users/profiles/minecraft/{username}'
        uuid = _response(url)
        return uuid['id']

    def _active_auctions(api_key, Uuid):
        "Returns a list of the player's active auctions, as well as information about the auctions, given an api key and the uuid of the player."
        requested_auctions_url = f'https://api.hypixel.net/skyblock/auction?key={api_key}&profile={ProfileID(Uuid)}'
        auctions = _response(requested_auctions_url)['auctions']
        for item in auctions:
            id = item['_id']
            uuid = item['uuid']
            auctioneer = item['auctioneer']
            profile_id = item['profile_id']
            coop = list(item['coop']) #this is a list
            start = item['start']
            end = item['end']
            item_name = item['item_name']
            item_lore = item['item_lore']
            extra = item['extra']
            category = item['category']
            tier = item['tier']
            starting_bid = item['starting_bid']
            item_bytes = item['item_bytes']['data']
            claimed = item['claimed']
            claimed_bidders = list(item['claimed_bidders']) #this is a list
            highest_bid_amount = item['highest_bid_amount']
            bids = list(item['bids']) #this is a list
        return id, uuid, auctioneer, profile_id, coop, start, end, item_name, item_lore, extra, category, tier, starting_bid, item_bytes, claimed, claimed_bidders, bin, highest_bid_amount, bids, profile_id
    
    def _auction_info(auction_uuid):
        "Returns various info about the auction"
        url = f'https://sky.coflnet.com/api/auction/{auction_uuid}'
        response = _response(url)

        enchantments = list(response['enchantments'])
        uuid = response['uuid']
        count = int(response['count'])
        startingBid = int(response['startingBid'])
        tag = response['tag']
        itemName = response['itemName']
        start = response['start']
        end = response['end']
        auctioneerId = response['auctioneerId']
        profileId = response['profileId']
        highestBidAmount = int(response['highestBidAmount'])
        bids = list(response['bids'])
        for bid in bids:
            bidder = bid['bidder']
            profileId = bid['profileId']
            amount = int(bid['amount'])
            timestamp = bid['timestamp']
        anvilUses = response['anvilUses']
        nbtData = response['nbtData']
        itemCreatedAt = response['itemCreatedAt']
        reforge = response['reforge']
        category = response['category']
        tier = response['tier']
        bin = response['bin']
        flatNbt = response['flatNbt']

        return enchantments, uuid, count, startingBid, tag, itemName, start, end, auctioneerId, profileId, highestBidAmount, bids, bidder, profileId, amount, timestamp, anvilUses, nbtData, itemCreatedAt, reforge, category, tier, bin, flatNbt

    def _past_sales(uid):
        "Returns a list of the past sales of the specified item, given its uid."
        url = f'https://sky.coflnet.com/api/auctions/uid/{uid}/sold'
        response = _response(url)
        past_sales = list(response['pastSales'])
        for item in past_sales:
            seller = item['seller']
            uuid = item['uuid']
            buyer = item['buyer']
            timestamp = item['timetamp']
        return seller, uuid, buyer, timestamp




            

            






            

