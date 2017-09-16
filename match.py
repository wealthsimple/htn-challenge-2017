import json

def match_ratio(filename):
    with open(filename) as f:
        data = json.load(f)
#     print(data)
    target = data['target_allocations']
    portfolio = data['portfolio_holdings']
    assets = data['asset_prices']
    keys = [key for key in target.keys()]
    values = [portfolio[key]*assets[key] for key in target.keys()]
#     print(values)
    total_values = sum(values)
#     print(total_values)
    target_values = [total_values*target[key] for key in target.keys()]
#     print(target_values)
    # equalize
    for i in range(len(target_values)):
        if values[i] < target_values[i]:
            amount = 0
            amount = (-values[i] + target_values[i])/assets[keys[i]]
              
            print("BOUGHT " + str(amount) + " units of " + keys[i])
            #but
        elif values[i] > target_values[i]:
            # sell
            amount = (values[i] - target_values[i])/assets[keys[i]]
            print("SOLD " + str(amount) + " units of " + keys[i])

match_ratio('test-data-1.json')
