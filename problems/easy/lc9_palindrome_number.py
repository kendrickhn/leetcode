class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = 0
        if x < 0: 
            return False
        else: 
            for i in range(len(str(x))-1,-1,-1): 
                y += int(str(x)[i]) * (10**i)
            if y == x: 
                return True  
            else: 
                return False
