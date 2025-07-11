# solved in 11:27
class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = ['a','A','e','E','i','I','o','O','u','U']
        vowl = []
        new_list = ''
        a = -1
        for i in range(len(s)):
            if s[i] in vow:
                vowl.append(s[i])
        for i in range(len(s)): 
            if s[i] in vow: 
                new_list += vowl[a]
                a -= 1
            else: 
                new_list += s[i]
        return new_list




        