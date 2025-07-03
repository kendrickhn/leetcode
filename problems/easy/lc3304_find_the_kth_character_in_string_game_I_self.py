# 8:26
import string
class Solution:
    def kthCharacter(self, k: int) -> str:
        x = 'a'
        while len(x) < k: 
            for i in x: 
                if i != 'z':
                    x = x + str(string.ascii_lowercase[string.ascii_lowercase.index(i)+1])
                if i == 'z': 
                    x = x + 'a'
        return x[k-1]
            