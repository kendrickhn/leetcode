class Solution:
    def reverseWords(self, s: str) -> str:
        n = s.split()
        m = ''
        i = -1
        if len(n) == 1:
            return n[0]
        while i > -len(n): 
            m += n[i] + ' '
            i -= 1
        m += n[i]
        return m

