# htn-challenge-2017

At Wealthsimple, portfolios have a specified distribution of asset holdings called a `target_allocation`. This allocation is based on the total value of the asset. For example, a 50/50 allocation between asset A and asset B means the total value of all the asset A you hold is equal to the total value of all the asset B you hold.

When the market price of certain assets change, the account deviates from its `target_allocation`. When this happens, we can restore the specified balance of assets by buying and selling stocks so that the desired ratio of assets is recovered.


### Challenge

Given a portfolio's `target_allocation (ratio of assets)`, `portfolio_holdings (number of each asset)`, and `asset_prices (the cost per unit of the asset)`, generate a series of trades to ensure the portfolio is balanced according to the `target_allocation`.

BONUS: We don't want to increase operating costs by doing penny trades. If an asset is within 0.5% of its target allocation, do not trade that asset.

BONUS BONUS: Although Wealthsimple can trade fractions of an asset, not all brokerages can. Apply this restriction to your code and get as close to the target allocation as possible.


### Specifications
You must create a script in Python3, Ruby, or Javascript. This script should read from a file containing test data like the test cases provided, and the name of the file should be configurable.

The output of the script should be a list of trades generated, formatted like the following example:

```
We placed 3 trades:
1. Bought 120 units of XIC
2. Sold 45 units of ZFM
3. Sold 20 units of VUS
```
