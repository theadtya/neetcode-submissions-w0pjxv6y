class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset= set(nums)
        longest=0
        
        for num in numset:
            length=1
            curr= num-1
            while curr in numset:
                length+=1
                curr-=1
            longest= max(length,longest)
        return longest