# solved in 8:21
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = 0
        n = ''
        o = ''
        if len(word1) >= len(word2): 
            n = word1
            m = word2
        elif len(word1) < len(word2): 
            n = word2
            m = word1
        for i in range(len(m)): 
            o += word1[i]
            o += word2[i]
        for i in range(len(m),len(n)): 
            o += n[i]
        return o



