class Solution(object):
    def countSubarrays(self, num):
        count = 0
        for i in range(len(num) - 2):
            a = num[i]
            b = num[i+1]
            c = num[i+2]
            
            if (a + c)*2 == b: 
                count +=1
        return count