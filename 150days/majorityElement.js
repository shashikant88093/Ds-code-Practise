// Input: nums = [3,2,3]
// Output: 3
// Example 2:

// Input: nums = [2,2,1,1,1,2,2]
// Output: 2


const majorityElement = function (nums) {
    let obj = {}

    for (let i = 0; i < nums.length; i++) {
        if (obj[nums[i]] === undefined) {
            obj[nums[i]] = 1
        } else {
            obj[nums[i]]++
        }
    }
    console.log(obj)

    let maxKey = null;
    let maxValue = -Infinity;

    for (let key in obj) {
      
        if (obj[key] > maxValue) {
            maxValue = obj[key];
            maxKey = key;
        }
    }

    return maxKey

}
let nums = [3, 2, 3]
console.log(majorityElement(nums))


// var majorityElement = function(nums) {
//     let el = -1;
//     let count = 0;
//     for(let i=0; i<nums.length; i++){
//         if(count == 0) {
//             el = nums[i];
//             count = 1;
//             continue;
//         }
//         if(el != nums[i]) count--;
//         else count++;
//     }
//     return el;
    
// };