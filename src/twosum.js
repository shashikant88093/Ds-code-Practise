function twoSum(nums,target){
    let map = new Map()
    for(let i=0;i<nums.length;i++){
        let comp = target - nums[i]
        console.log(comp,"comp")
        console.log(map.has(comp),"map.has(comp)")
        if(map.has(comp)){
            console.log(map,"inside map")
            return [map.get(comp),i]
        }
        map.set(nums[i],i)
    }
    console.log(map,"map")
}

let result = twoSum([2,7,11,15],9)
console.log(result)