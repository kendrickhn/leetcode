class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for c in range(len(nums)):
            b = target - nums[c]
            a = []
            a.append(c)
            if b in nums and nums.index(b) != c:
                a.append(nums.index(b))
                return a
             
                
