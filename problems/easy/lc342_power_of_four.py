class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n & (n-1) == 0 and n != 0: 
            x = math.log(n) / math.log(2)
            if x % 2 == 0: 
                return True 
        return False
        