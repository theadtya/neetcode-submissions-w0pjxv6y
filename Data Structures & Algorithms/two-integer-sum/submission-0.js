class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
    const compMap= new Map();
    for(let i =0;i<nums.length;i++){
        if(compMap.has(target-nums[i])){
            return [i,compMap.get(target-nums[i])];
        }
        compMap.set(nums[i],i);
    }
    }
}
