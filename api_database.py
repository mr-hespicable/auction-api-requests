import io, requests, os, nbt, base64


class get:
    def __response(call):
        r = requests.get(call)
        return r.json()

    def __ProfileStats(uuid):
        profiles = get.response(f'https://sky.shiiyu.moe/api/v2/profile/{uuid}')['profiles']
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
        return get.ProfileStats(uuid)[0]

    def ProfileID(uuid):
        'Returns the id of the profile, given a uuid.'
        return get.ProfileStats(uuid)[1]
    
