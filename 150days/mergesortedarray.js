let num1 = [1, 2, 3, 0, 0, 0];
let num2 = [2, 5, 6];
let m = 3;
let n = 3;

var merge = function(nums1, m, nums2, n) {
    let i = m - 1;
    let j = n - 1;
    let k = m + n - 1;

    // Merge nums2 into nums1 starting from the end
    while (i >= 0 && j >= 0) {
        if (nums1[i] > nums2[j]) {
            nums1[k] = nums1[i];
            i--;
        } else {
            nums1[k] = nums2[j];
            j--;
        }
        k--;
    }

    // If there are remaining elements in nums2, copy them
    while (j >= 0) {
        nums1[k] = nums2[j];
        j--;
        k--;
    }
};

merge(num1, m, num2, n);
console.log(num1); // Output: [1, 2, 2, 3, 5, 6]