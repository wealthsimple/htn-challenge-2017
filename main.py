import json
import io

MAX = 10000
if __name__ == '__main__':
    with io.open('./test/test-data-1.json') as f:
        data = json.loads(f.read())
    target = {}
    total_money = 0

    for name in data['target_allocations'].keys():
        total_money += data['portfolio_holdings'][name] * data['asset_prices'][name]

    for name in data['target_allocations'].keys():
        current_holdings_percentage = abs(data['asset_prices'][name] * data['portfolio_holdings'][name]) / total_money
        if abs(current_holdings_percentage - data['target_allocations'][name ]) < 0.005:
            # don't trade
            target[name] = data['portfolio_holdings'][name]
            continue
        curr = 0
        curr_diff = abs(total_money * data['target_allocations'][name] - (curr * data['asset_prices'][name]))
        next_diff = abs(total_money * data['target_allocations'][name] - ((curr + 1) * data['asset_prices'][name]))
        while next_diff < curr_diff:
            curr += 1
            curr_diff = abs(total_money * data['target_allocations'][name] - (curr * data['asset_prices'][name]))
            next_diff = abs(total_money * data['target_allocations'][name] - ((curr + 1) * data['asset_prices'][name]))

        target[name] = curr

    total_trades = 0
    for name in data['target_allocations'].keys():
        if target[name] != data['portfolio_holdings'][name]:
            total_trades += 1
    print "We placed", total_trades, "trades:"
    for i in range(len(data['target_allocations'].keys())):
        name = data['target_allocations'].keys()[i]
        if target[name] - data['portfolio_holdings'][name] > 0:
            print str(i + 1) + '. Bought', target[name] - data['portfolio_holdings'][name], 'units of', name
        elif target[name] - data['portfolio_holdings'][name] < 0:
            print str(i + 1) + '. Sold', data['portfolio_holdings'][name] - target[name], 'units of', name
