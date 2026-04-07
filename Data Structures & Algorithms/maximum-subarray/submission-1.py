class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum=maxsum=nums[0]
        for num in nums[1:]:
            currsum= max(currsum+num, num)
            maxsum= max(currsum,maxsum)
        return maxsum
