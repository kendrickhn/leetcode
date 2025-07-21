class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        if len(nums) == 1: 
            return 0
        a = 0
        b = len(nums) - 1
        count = 0
        s = 0
        while a != b and a < b: 
            s = nums[a] + nums[b]
            if s > k: 
                b -= 1
            elif s == k: 
                a += 1
                b -= 1
                count += 1
            elif s < k: 
                a += 1
        return count
        

        