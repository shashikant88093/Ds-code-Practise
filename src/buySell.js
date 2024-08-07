// // ?input  7,1,5,3,6,4
// // output 5
// // 4 -7 = -3  , 6-1 =5 , 3-5 = -2

// function buysell(prices){
//     let minPrice = Infinity;
//     let maxProfit = 0;

//     // Iterate through each price using a traditional for loop
//     for (let i = 0; i < prices.length; i++) {
//         let price = prices[i];
        
//         // Update minPrice to the minimum of the current minPrice and the current price
//         if (price < minPrice) {
//             minPrice = price;
//         }
        
//         // Calculate the profit if selling at the current price
//         let profit = price - minPrice;
        
//         // Update maxProfit if the current profit is greater than the previous maxProfit
//         if (profit > maxProfit) {
//             maxProfit = profit;
//         }
//     }

//     // Return the maximum profit found
//     return maxProfit;
// }


// // let result = buysell([7,1,5,3,6,4])
// let result = buysell([7,6,4,3,1])

// console.log(result)


var maxProfit = function(prices) {
    // var maxPrice = 0; 
    // for(var i = 0; i < prices.length; i++){
    //     for(var j = i + 1; j < prices.length; j++){
    //         if(prices[j] - prices[i] > maxPrice){
    //             maxPrice = prices[j] - prices[i]
    //         }
    //     }
    // }
    // return maxPrice

    let buy= prices[0]; 
    let profit = 0; 

    for(let i = 1; i < prices.length; i++){
        console.log(buy,"buy")
        if(prices[i] < buy){
        console.log(prices[i],"prices[i]")

            buy = prices[i]; 
        } else if(prices[i] - buy > profit){
        console.log( prices[i] - buy," prices[i] - buy")

            profit = prices[i] - buy
        }
    }
    return profit 
    
}

console.log(maxProfit([7,1,5,3,6,4]))