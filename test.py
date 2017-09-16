import json
from pprint import pprint

with open('./test/test-data-1.json') as data_file:    
    data = json.load(data_file)

data2 = []
tot = 0

for s in data['asset_prices']:
    data2.append({
        'a': data['asset_prices'][s], 
        'p': data['portfolio_holdings'][s],
        'd': data['target_allocations'][s],
        'delta': 0
    })
    tot += data['portfolio_holdings'][s] * data['asset_prices'][s]

trades = 0

for s in data2:
    while abs(s['d'] - (s['p'] + s['delta']) * s['a'] * 1.0 / tot) > 0.005:
        if s['d'] - (s['p'] + s['delta']) * s['a'] * 1.0 / tot > 0:
            # Need to buy
            s['delta'] += 1
        else:
            s['delta'] -= 1
        trades += 1

print('Trades: ', trades)
for s in data2:
    if s['delta'] == 0:
        continue
    print(s)


