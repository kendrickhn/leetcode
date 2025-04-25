from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums, modulo, k):
        count = defaultdict(int)
        count[0] = 1  # base case
        prefix = 0
        result = 0
        
        for num in nums:
            if num % modulo == k:
                prefix += 1
            # normalize mod
            mod_val = prefix % modulo
            target = (mod_val - k) % modulo
            result += count[target]
            count[mod_val] += 1
            
        return result
