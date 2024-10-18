// Input: prices = [7,1,5,3,6,4]
// Output: 7
// Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
// Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
// Total profit is 4 + 3 = 7.


function maxProfit(prices) {

    let profit = 0
    for (let i = 0; i < prices.length-1; i++) {
        // console.log(price,"price")
        if (prices[i] < prices[i + 1]) {
            let gain = prices[i + 1] - prices[i];
            profit += gain
        }


    }
    return profit

}

let prices = [7, 1, 5, 3, 6, 4]
// let prices = [1,2,3,4,5]
// let prices = [7,6,4,3,1]

console.log(maxProfit(prices))