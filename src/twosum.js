// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


function twoSum(nums, target) {
    const map = new Map();
    for (let i = 0; i < nums.length; i++) {


        const complement = target - nums[i]
        console.log(complement, "complement")
        if (map.has(complement)) {
            return [map.get(complement), i]
        }

        console.log(complement, "complement@@@@@@@@@@@@@@")

        map.set(nums[i], i)
        console.log(map, "map")
    }

    throw new Error("No two sum solution");
}

const nums = [2, 7, 11, 15];
const target = 9;
const result = twoSum(nums, target);
console.log(result); // Output: [0, 1]


// function twoSum(nums, target) {
//     const map = new Map();

//     for (let i = 0; i < nums.length; i++) {
//         const complement = target - nums[i];

//         if (map.has(complement)) {
//             return [map.get(complement), i];
//         }

//         map.set(nums[i], i);
//     }

//     throw new Error("No two sum solution");
// }

// // Example usage:
// const nums = [2, 7, 11, 15];
// const target = 9;
// const result = twoSum(nums, target);
// console.log(result); // Output: [0, 1]
