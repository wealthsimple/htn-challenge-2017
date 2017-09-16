import sys, json

data = json.load(sys.stdin)

# Get total value of portfolio
total = 0

for key, value in data["portfolio_holdings"].iteritems():
    total += value * data["asset_prices"][key]

trades = 0
output = []
for key, value in data["target_allocations"].iteritems():
    delta = data["portfolio_holdings"][key] * data["asset_prices"][key] - value * total
    # check 0.5%
    if abs(delta) > 0.005 * abs(value*total):
        if delta > 0:
            output.append(str(trades + 1) + ". Sold " + str(delta/data["asset_prices"][key]) + " units of " + key)
            trades += 1
        elif delta < 0:
            output.append(str(trades + 1) + ". Bought " + str(abs(delta/data["asset_prices"][key])) + " units of " + key)
            trades += 1

output.insert(0, "We placed " + str(trades) + " trades:")

for line in output:
    print(line)