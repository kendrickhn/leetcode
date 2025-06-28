class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        for i in range(len(nums)-k): 
            a = min(nums)
            nums.remove(a)
        return nums
