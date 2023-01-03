import api_database as api

uuid = api.get.uuid('websafe')

active_auctions = api.get._active_auctions('73d5e91d-77c2-4df2-97fd-5da88f16ed8e', uuid, 2)

id = active_auctions[0]
uuid = active_auctions[1]
auctioneer = active_auctions[2]
profile_id = active_auctions[3]
coop = active_auctions[4]
start = active_auctions[5]
end = active_auctions[6]
item_name = active_auctions[7]
item_lore = active_auctions[8]
extra = active_auctions[9]
category = active_auctions[10]
tier = active_auctions[11]
starting_bid = active_auctions[12]
item_bytes = active_auctions[13]
claimed = active_auctions[14]
claimed_bidders = active_auctions[15]
highest_bid_amount = active_auctions[16]
bids = active_auctions[17]




