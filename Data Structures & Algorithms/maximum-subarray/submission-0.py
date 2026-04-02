class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=currsum=nums[0]
        for num in nums[1:]:
            currsum= max(currsum+num,num)
            maxsum=max(maxsum,currsum)
        return maxsum