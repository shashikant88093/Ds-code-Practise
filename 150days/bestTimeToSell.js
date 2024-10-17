var maxProfit = function(prices) {
    let minPrice = Infinity;
    let maxProfit = 0;

    // Iterate through each price using a traditional for loop
    for (let i = 0; i < prices.length; i++) {
        let price = prices[i];
        
        // Update minPrice to the minimum of the current minPrice and the current price
        console.log(price < minPrice,"check price and minprice compare")
        if (price < minPrice) {
            minPrice = price;
        }
        
        // Calculate the profit if selling at the current price
        let profit = price - minPrice;
        
        // Update maxProfit if the current profit is greater than the previous maxProfit
        if (profit > maxProfit) {
            maxProfit = profit;
        }
    }

    // Return the maximum profit found
    return maxProfit;
};

let prices =  [7,1,5,3,6,4]
console.log(maxProfit(prices))