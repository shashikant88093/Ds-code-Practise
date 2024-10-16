// Input: nums = [1,2,3,4,5,6,7], k = 3
// Output: [5,6,7,1,2,3,4]
// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]
// rotate 2 steps to the right: [6,7,1,2,3,4,5]
// rotate 3 steps to the right: [5,6,7,1,2,3,4]


function rotateArr(nums,k){

    k = k % nums.length;
    function reverse(start, end) {
      while (start < end) {
        [nums[start], nums[end]] = [nums[end], nums[start]];
        start++;
        end--;
      }
    }
  
    reverse(0, nums.length - 1);
    reverse(0, k - 1);
  
    reverse(k, nums.length - 1);
  
    return nums;
}


let nums =  [1,2,3,4,5,6,7]

let k = 3

console.log(rotateArr(nums,k))