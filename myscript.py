import json

FILE_NAME = "test-data-1.json"

def trade(target, portfolio, asset, name):
	assetVals = [asset[i]*portfolio[i] for i in range(len(asset))]
	totalVal = sum(assetVals)
	diff = [assetVals[i]/totalVal - target[i] for i in range(len(asset))]
	trade = []
	for i in range(len(diff)):
		if abs(diff[i]) < 0.005:
			continue
		else:
			targeted = target[i] * totalVal - assetVals[i]
			buy = targeted > 0
			if buy:
				buy = 1
			else:
				buy = 0
			targeted = abs(targeted)
			quant = round(targeted/asset[i])
			trade.append((buy, quant))
	print("We placed {0} trades:".format(len(trade)))
	trade = sorted(trade, key=lambda x: x[1])
	for i in range(1, len(trade)+1):
		print(("{0}. " + ("Bought" if trade[i-1][0] else "Sold") + " {1} units of {2}").format(i, trade[i-1][1], name[i-1]))

def loadFile(f):
	f = open(f, "r")
	j = json.loads(f.read())
	trade([j["target_allocations"][i] for i in j["target_allocations"]], [j["portfolio_holdings"][i] for i in j["portfolio_holdings"]], [j["asset_prices"][i] for i in j["asset_prices"]], [i for i in j["asset_prices"].keys()])

loadFile("test/" + FILE_NAME)
