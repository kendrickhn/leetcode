# LeetCode Problem: 2597. The Number of Fair Pairs
# Tags: Binary Search, Sorting, Two Pointers
# Solved with AI assistance

from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        n = len(nums)
        res = 0

        for i in range(n):
            left = bisect_left(nums, lower - nums[i], i + 1, n)
            right = bisect_right(nums, upper - nums[i], i + 1, n)
            res += right - left

        return res

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.countFairPairs([0,1,7,4,4,5], 3, 6))  # Output: 6
    print(sol.countFairPairs([1,7,9,2,5], 11, 11))  # Output: 1
