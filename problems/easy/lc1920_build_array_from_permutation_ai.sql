from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Encode both old and new values into each slot:
        # new_val = nums[nums[i]] % n
        # store as: nums[i] = old_val + new_val * n
        for i in range(n):
            nums[i] += (nums[nums[i]] % n) * n
        
        # Decode to recover new_val in-place:
        for i in range(n):
            nums[i] //= n
        
        return nums
