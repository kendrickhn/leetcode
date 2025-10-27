class Solution(object):
    def findNumbers(self, nums):
        count = 0 
        for num in nums:
            length = len(str(num))
            if length % 2 == 0:
                count = count + 1 
        return count