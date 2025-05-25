from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # We actually don't need the tree structure (edges) for the XOR pairing logic
        orig_sum = sum(nums)
        # Compute delta = (nums[i] ^ k) - nums[i] for each node
        deltas = [(x ^ k) - x for x in nums]
        
        # Separate positive gains and negative losses
        pos = [d for d in deltas if d > 0]
        neg = [d for d in deltas if d < 0]
        
        pos_sum = sum(pos)
        cnt = len(pos)
        
        # If we can pick an even number of nodes to flip, just take all positive deltas
        if cnt % 2 == 0:
            return orig_sum + pos_sum
        
        # Otherwise we need to drop one flip to make the count even:
        # either drop the smallest positive gain, or include one smallest-loss (i.e. largest negative)
        min_pos = min(pos) if pos else float('inf')
        max_neg = max(neg) if neg else float('-inf')
        # The penalty is the smaller of these two options
        penalty = min(min_pos, -max_neg)
        
        return orig_sum + pos_sum - penalty