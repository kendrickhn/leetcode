class Solution:
    def maximum69Number (self, num: int) -> int:
        c = str(num)
        l = len(c)
        i = 0
        a = False
        while i < l and a == False:
            if c[i] == '6': 
                a = True
            else:
                i += 1
        if a != False: 
            b = c[:i] + '9' + c[i+1:]
            return int(b)
        else: 
            return num
