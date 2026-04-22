class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        n= len(nums)
        target=0
        for i in range(n):
            if nums[i] > target:
                break
            if i>0 and nums[i]== nums[i-1]:
                continue
            l,r= i+1, n-1
            while l<r:
                total= nums[i]+ nums[l] + nums[r]
                if total < target:
                    l+=1
                elif total > target:
                    r-=1
                else:
                    res.append([nums[i],nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]== nums[l-1]:
                        l+=1
                    while l<r and nums[r]== nums[r+1]:
                        r-=1
        return res
                

                    







