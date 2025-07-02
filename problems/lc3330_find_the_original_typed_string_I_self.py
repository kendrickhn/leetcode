class Solution:
    def possibleStringCount(self, word: str) -> int:
        a = 1
        b = []
        for i in range(len(word)): 
            if word[i] in b and word[i-1] == word[i]: 
                a += 1
            else: 
                b.append(word[i])
        return a

