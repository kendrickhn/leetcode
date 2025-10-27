class Solution:
    def isZeroArray(self, nums, queries):
        n = len(nums)
        # 1) Build a difference array to count how many queries cover each index
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1
        
        # 2) Prefix-sum to get cover count c[j] for each position j
        cover = [0] * n
        curr = 0
        for j in range(n):
            curr += diff[j]
            cover[j] = curr
        
        # 3) Check feasibility: each nums[j] requires exactly nums[j] decrements,
        #    and there are cover[j] opportunities. Must have cover[j] >= nums[j].
        for j in range(n):
            if cover[j] < nums[j]:
                return False
        
        return True
