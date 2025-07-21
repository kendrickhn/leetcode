class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = 0
        b = 0
        while a < len(s) and b < len(t): 
            if t[b] == s[a]: 
                a += 1
                b += 1
            elif t[b] != s[a]: 
                b += 1
        else: 
            if a == len(s): 
                return True
            elif b == len(t): 
                return False

        