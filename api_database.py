import io, requests, os, nbt, base64



def __response(call):
    r = requests.get(call)
    return r.json()

def __ProfileStats(uuid):
    url = f'https://sky.shiiyu.moe/api/v2/profile/{uuid}'
    profiles = __response(url)['profiles']
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

class get_auctions:
    def requested(api_key, profile_id, uuid):
        url = f'https://api.hypixel.net/skyblock/auction?key={api_key}&profile={ProfileID()}'

    
