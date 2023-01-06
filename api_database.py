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

<<<<<<< Updated upstream
def ProfileName(uuid):
    'Returns the name of the skyblock profile, given a uuid.'
    return __ProfileStats(uuid)[0]
def ProfileID(uuid):
    'Returns the id of the skyblock profile, given a uuid.'
    return __ProfileStats(uuid)[1]
=======
>>>>>>> Stashed changes

def decode(raw_data):
    return nbt.nbt.NBTFile(fileobj=io.BytesIO(base64.b64decode(raw_data)))
def id(nbt_data):
    extra = nbt_data.tags[0].tags[0]['tag']['ExtraAttributes']
    return extra['id']
def name(nbt_data):
    z = nbt_data.tags[0].tags[0]['tag']['ExtraAttributes']
    if str(z['id']) == 'PET':
        petName = _response(str(z['petInfo']))['type']
        return petName

class give:
    def _ProfileName(uuid):
        'Returns the name of the profile, given a uuid.'
        return __ProfileStats(uuid)[0]
    def _ProfileID(uuid):
        'Returns the id of the profile, given a uuid.'
        return __ProfileStats(uuid)[1]

class _baseAPI:
    profileName = give._ProfileName()
    profileID = give._ProfileID()
    """
    Base class for API
    """
    def uuid(username):
        "Returns the name and uuid of the player, given a username."
        url = f'https://api.mojang.com/users/profiles/minecraft/{username}'
        uuid = _response(url)
        return uuid['id']

<<<<<<< Updated upstream
    def active_auctions(api_key, Uuid):
=======
    def active_auctions(username, api_key):
>>>>>>> Stashed changes
        """
        Gives a list of the player's active auctions, as well as information about the auctions.
        NEEDS: api_key, uuid
        """
        requested_auctions_url = f'https://api.hypixel.net/skyblock/auction?key={api_key}&profile={give._ProfileID(uuid(username))}'
        auctions = _response(requested_auctions_url)['auctions']

        id = auctions['_id']
        uuid = auctions['uuid']
        auctioneer = auctions['auctioneer']
        profile_id = auctions['profile_id']
        coop = auctions['coop'] #this is a list
        start = auctions['start']
        end = auctions['end']
        item_name = auctions['item_name']
        item_lore = auctions['item_lore']
        extra = auctions['extra']
        category = auctions['category']
        tier = auctions['tier']
        starting_bid = auctions['starting_bid']
        item_bytes = auctions['item_bytes']['data']
        claimed = auctions['claimed']
        claimed_bidders = auctions['claimed_bidders'] #this is a list
        highest_bid_amount = auctions['highest_bid_amount']
        bids = auctions['bids'] #this is a list
<<<<<<< Updated upstream
=======
        
        return id, uuid, auctioneer, profile_id, coop, start, end, item_name, item_lore, extra, category, tier, starting_bid, item_bytes, claimed, claimed_bidders, highest_bid_amount, bids
>>>>>>> Stashed changes
    def auction_info(auction_uuid):
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
    def past_sales(uid):
        "Returns a list of the past sales of the specified item, given its uid."
        url = f'https://sky.coflnet.com/api/auctions/uid/{uid}/sold'
        response = _response(url)
        past_sales = list(response['pastSales'])
        for item in past_sales:
            return item['seller'], item['uuid'], item['buyer'], item['timestamp']


        
        
