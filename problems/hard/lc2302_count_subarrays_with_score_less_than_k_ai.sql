class Solution:
    def countSubarrays(self, nums, k):
        n = len(nums)
        left = 0
        total = 0
        running_sum = 0

        for right in range(len(nums)):
            running_sum += nums[right]
            while running_sum * (right - left + 1) >= k:
                running_sum -= nums[left]
                left += 1
            total += (right - left + 1)

        return total
