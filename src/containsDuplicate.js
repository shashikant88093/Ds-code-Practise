// [1,2,3,1] return false

function containsDuplicate(nums){
let map = new Map()
for(let i=0;i<nums.length;i++){
    map.set(nums[i],i)
}
if(map.size === nums.length){
    return false
}
return true
}

console.log(containsDuplicate([1,2,3,1]))