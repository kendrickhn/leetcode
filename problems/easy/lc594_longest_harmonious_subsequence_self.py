# class Solution:
#     def findLHS(self, nums: List[int]) -> int:
#         x = 0
#         i = 0
#         while i <= len(nums)-1: 
#             if nums[i] in nums and nums[i]+1 in nums:
#                 lst = []
#                 for a in nums: 
#                     if a == nums[i] or a == nums[i]+1:
#                         lst.append(a)
#                         y = len(lst)
#                         if y > x: 
#                             x = y
#                 i += 1 
#             else: 
#                 i += 1
#         return x
            
                
# class Solution:
#     def findLHS(self, nums: List[int]) -> int:  
#         x = 0 
#         for i in nums:      
#             lst = []
#             if i in nums and i + 1 in nums:
#                 for a in nums: 
#                     if a == i or a == i+1: 
#                         lst.append(a)
#                 b = len(lst)
#                 if b > x:
#                     x = b 
#         return x

from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_len = 0
        for num in freq:
            if num + 1 in freq:
                max_len = max(max_len, freq[num] + freq[num + 1])
        return max_len  

        