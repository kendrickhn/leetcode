class Solution:
    def countSubarrays(self, nums, minK, maxK):
        res = 0
        last_min = last_max = bad = -1
        
        for i, num in enumerate(nums):
            if not (minK <= num <= maxK):
                bad = i
            if num == minK:
                last_min = i
            if num == maxK:
                last_max = i
            res += max(0, min(last_min, last_max) - bad)
        
        return res
