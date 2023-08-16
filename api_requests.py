import io, requests, os, nbt, base64

def _response(call):
    r = requests.get(call)
    return r.json()
def _ProfileStats(uuid):
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

class get:
    def _ProfileName(uuid):
        'Returns the cute name of the profile, given a uuid.'
        return _ProfileStats(uuid)[0]
    def _ProfileID(uuid):
        'Returns the id of the profile, given a uuid.'
        return _ProfileStats(uuid)[1]
    def uuid(username):
        "Returns the uuid of the player, given a username."
        url = f'https://api.mojang.com/users/profiles/minecraft/{username}'
        uuid = _response(url)
        return uuid['id']


skyblockResourcesURL = f'https://api.hypixel.net/resources/skyblock/'
def getCollectionInfo():
        return _response(skyblockResourcesURL + 'collections')
def getSkillInfo(): 
    return _response(skyblockResourcesURL + 'skills')
def getItemInfo():
    return _response(skyblockResourcesURL + 'items')
def getElectionInfo():
    return _response(skyblockResourcesURL + 'election')
def getBingoInfo():
    return _response(skyblockResourcesURL + 'bingo')

class info:
    def __init__(self, name, api_key):
        self.name = name
        self.api_key = api_key