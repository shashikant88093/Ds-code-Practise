
// Input: nums = [2,3,1,1,4]
// Output: 2
// Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

const jumpGame2 = (nums) => {
    if (nums.length <= 1) return 0; // If the array length is 1 or less, no jump is needed.

    let jumps = 0; // Number of jumps needed to reach the end.
    let currentEnd = 0; // End of the range that we can reach with the current jump.
    let farthest = 0; // The farthest point we can reach with the next jump.

    for (let i = 0; i < nums.length - 1; i++) {
        farthest = Math.max(farthest, i + nums[i]);

        // If we reach the end of the range for the current jump, we must jump again.
        if (i === currentEnd) {
            jumps++;
            currentEnd = farthest;

            // If the currentEnd reaches or exceeds the last index, we can stop early.
            if (currentEnd >= nums.length - 1) {
                break;
            }
        }
    }

    return jumps;
}

let nums = [2, 3, 1, 1, 4]

console.log(jumpGame2(nums))