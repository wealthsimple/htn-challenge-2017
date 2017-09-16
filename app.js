var data = require('./test/test-data-2.json');

const ALLOW_FRACTIONAL_SHARES = true;

var data2 = {};

var total_asset = 0;
for (var key in data.target_allocations) {
  total_asset += data.portfolio_holdings[key] * data.asset_prices[key];
}

for (var key in data.target_allocations) {
  data2[key] = {
    actual: data.portfolio_holdings[key] * data.asset_prices[key],
    ideal: data.target_allocations[key] * total_asset
  }
}

var excess = 0;
for (var key in data2) {
  const diff = data2[key].actual - data2[key].ideal;
  if (diff / data2[key].ideal >= 0.05) {
    var quant = Math.abs(diff / data.asset_prices[key]);
    if (ALLOW_FRACTIONAL_SHARES) {
      quant = Math.floor(quant);
    }
    excess += quant * data.asset_prices[key];
    data.portfolio_holdings[key] -= quant;
    console.log(`Selling ${quant} shares of ${key}.`);
  }
}

for (var key in data2) {
  const diff = data2[key].actual - data2[key].ideal;
  if (diff / data2[key].ideal >= 0.05) {
    var quant = Math.abs(diff / data.asset_prices[key]);
    if (ALLOW_FRACTIONAL_SHARES) {
      quant = Math.floor(quant);
    }
    var actualQuant = 0;
    while (excess > 0 && quant > 0) {
      quant--;
      actualQuant++;
      excess -= data.asset_prices[key];
    }
    data.portfolio_holdings[key] += actualQuant;
    console.log(`Buying ${actualQuant} shares of ${key}.`);
  }
}


var data3 = {};
for (var key in data.target_allocations) {
  data3[key] = {
    actual: data.portfolio_holdings[key] * data.asset_prices[key],
    ideal: data.target_allocations[key] * total_asset
  }
}
console.log('Portfolio: ', data);
console.log('Portfolio value: ', data3);
