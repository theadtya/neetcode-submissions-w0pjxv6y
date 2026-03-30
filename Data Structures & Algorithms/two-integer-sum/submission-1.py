class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comphash={}
        for i in range(len(nums)):
            comp= target-nums[i]
            if comp in comphash:
                return [comphash[comp],i]
            comphash[nums[i]]=i
        