# LeetCode 2176 - Count Equal and Divisible Pairs in an Array
# Solved by Self on 2025-04-14

class Solution:
    def countPairs(self, nums, k):
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        return count
