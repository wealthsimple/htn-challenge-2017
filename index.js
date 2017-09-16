const fs = require("fs");

let data = JSON.parse(fs.readFileSync("./test/test-data-2.json", "utf8"));

let total_price = 0;

let portfolio_names = Object.keys(data["portfolio_holdings"]);

let price_per_holding = {};

portfolio_names.forEach((portfolio_name) => {
	let portfolio_price = data["portfolio_holdings"][portfolio_name] * data["asset_prices"][portfolio_name];
	price_per_holding[portfolio_name] = portfolio_price;
	total_price += portfolio_price;
});


let desired_change_per_holding = {};
let desired_change = {};
portfolio_names.forEach((portfolio_name) => {
	let desired_portfolio_price = data["target_allocations"][portfolio_name] * total_price;
	desired_change[portfolio_name] = desired_portfolio_price;
	desired_change_per_holding[portfolio_name] =  desired_portfolio_price - price_per_holding[portfolio_name];
});

let needs_balance_queue = [];

Object.keys(desired_change_per_holding).forEach((portfolio_name) => {
	needs_balance_stack.push(portfolio_name)
	if(needs_balance_queue[0] !== portfolio_name) {
		let current_queue_first = desired_change_per_holding[needs_balance_stack[0]] / data["asset_prices"][needs_balance_stack[0]];
		let current_porfolio_desired_change = desired_change_per_holding[portfolio_name] / data["asset_prices"][portfolio_name];
		if(current_queue_first - current_porfolio_desired_change > current_queue_first) {
			
		}
	}
});