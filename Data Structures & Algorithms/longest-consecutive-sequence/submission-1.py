class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset= set(nums)
        longest=0
        
        for num in numset:
            if num-1 not in numset:
                curr=num
                length=1
                while curr+1 in numset:
                    curr+=1
                    length+=1
                longest= max(longest,length)
        return longest