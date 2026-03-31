class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(num):
            output=0
            while num:
                digit= num %10
                output+= digit **2
                num=num//10
            return output
        
        seen= set()
        while n not in seen:
            seen.add(n)
            n= sum_of_squares(n)
            if n==1:
                return True
        return False


