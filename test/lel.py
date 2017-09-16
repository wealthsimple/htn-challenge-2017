# Made by Jaimyn Mayer :) for the lightning talk
# hello@jaimyn.com.au

import json

with open('test-data-1.json') as data_file:    
    data = json.load(data_file)

values = {}

for holding_key, holding in data["portfolio_holdings"].items():
    for asset_key, asset in data["asset_prices"].items():
        values[holding_key] = asset * holding

print("Target Values")
for key, target in data["target_allocations"].items():
    
