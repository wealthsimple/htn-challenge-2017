import json
import math

with open("test-data-1.json", "r") as f:
	obj = json.loads(f.read())

print(obj["target_allocations"])

total = 0
for asset in obj["target_allocations"]:
	price = obj["target_asset_prices"][asset]
	holdings = obj["portfolio_holdings"][asset]
	total += price * holdings

sells = []
buys = []
for asset in obj["target_allocations"]:
	price = obj["target_asset_prices"][asset]
	holdings = obj["portfolio_holdings"][asset]
	current = price * holdings
	target = obj["target_allocations"][asset] * total
	if current/target < .95:
		buys.append((asset, math.floor((target - current) / price)))
	elif current/target > 1.05:
		sells.append((asset, math.ceil((current - target) / price)))	

i = 1
for s in sells:
	print "" + i + ". Sold " + s[1] + " units of " + s[0]
	i += 1
for b in buys:
	print "" + i + ". Bought " + b[1] + " units of " + b[0]
	i += 1
