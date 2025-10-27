class Solution:
    def largestGoodInteger(self, num: str) -> str:
        a = ''
        i = 1
        while i < len(num) -1: 
            if num[i] == num[i-1] and num[i] == num[i+1] and num[i] > a: 
                a = num[i]
            i += 1
        b = a + a + a
        if a == 0: 
            return ''
        else: 
            return b
            