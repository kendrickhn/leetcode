class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        rs = s
        if k == len(nums):
            return s / k
        for i in range(k,len(nums)):
            rs = rs - nums[i - k] + nums[i]
            if rs > s:
                s = rs
        return s / k
        