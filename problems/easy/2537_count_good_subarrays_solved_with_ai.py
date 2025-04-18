
from collections import defaultdict

class Solution:
    def countGood(self, nums, k):
        n = len(nums)
        total = 0
        left = 0
        count = defaultdict(int)
        pair_count = 0
        res = 0

        for right in range(n):
            val = nums[right]
            # Update pair count before incrementing count[val]
            pair_count += count[val]
            count[val] += 1

            # Shrink the window from left while pair_count >= k
            while pair_count >= k:
                res += n - right  # all subarrays from left to end are valid
                count[nums[left]] -= 1
                pair_count -= count[nums[left]]  # update AFTER reducing count
                left += 1

        return res

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.countGood([1,1,1,1,1], 10))  # Output: 1
    print(sol.countGood([3,1,4,3,2,2,4], 2))  # Output: 4
