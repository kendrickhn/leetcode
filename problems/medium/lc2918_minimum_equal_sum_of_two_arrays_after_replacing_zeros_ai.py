from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # 1) Compute sums ignoring zeros, and zero‐counts
        a = sum(x for x in nums1 if x != 0)
        b = sum(x for x in nums2 if x != 0)
        c = nums1.count(0)
        d = nums2.count(0)
        
        # 2) If neither has zeros, sums must already match
        if c == 0 and d == 0:
            return a if a == b else -1
        
        # 3) Candidate minimum S
        M = max(a + c, b + d)
        
        # 4) If nums1 has no zeros, its sum is fixed at a
        if c == 0:
            return a if M == a else -1
        
        # 5) If nums2 has no zeros, its sum is fixed at b
        if d == 0:
            return b if M == b else -1
        
        # 6) Otherwise both have zeros and M works
        return M
