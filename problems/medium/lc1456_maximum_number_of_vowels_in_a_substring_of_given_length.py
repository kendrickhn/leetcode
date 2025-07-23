class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        count = 0
        m = []
        while i < k: 
            m.append(s[i])
            if s[i] in 'aeiuo': 
                count += 1
            i += 1
        u = count
        for i in range(k,len(s)): 
            if m[0] in 'aeiou':
                count -= 1
            if s[i] in 'aeiou': 
                count += 1
            m.append(s[i])
            m.pop(0)
            if count > u: 
                u = count
        return u


        

        