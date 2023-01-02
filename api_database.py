import io, requests, os, nbt, base64

def response(call):
    r = requests.get(call)
    return r.json()

def prettify(string):
    return ('{:,}'.format(string))

def getProfileCuteName(api_key, uuid):
    profile_list = []
    for profile in response(f'https://api.hypixel.net/player?key={api_key}&uuid={uuid}')['player']['stats']['SkyBlock']['profiles']:
            name = response(f'https://api.hypixel.net/player?key={api_key}&uuid={uuid}')['player']['stats']['SkyBlock']['profiles'][profile]['cute_name']
            profile_list.append(name)
    length = len(profile_list)
    return length
        
list = getProfileCuteName('73d5e91d-77c2-4df2-97fd-5da88f16ed8e', '2e82ec5b72354497adfde07170979a72')
print(list)