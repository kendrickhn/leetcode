class Solution:
    def countSubarrays(self, nums, k):
        # 1. Find the global maximum X
        max_val = max(nums)
        
        # 2. Build an indicator array: 1 where nums[i] == X, else 0
        arr = [1 if num == max_val else 0 for num in nums]
        
        n = len(arr)
        result = 0      # total count of valid subarrays
        curr = 0        # current sum of arr[left:right]
        right = 0       # exclusive end pointer
        
        # 3. Two-pointer sliding window
        for left in range(n):
            # expand right until we have at least k ones
            while right < n and curr < k:
                curr += arr[right]
                right += 1
            
            # if even khi right == n vẫn chưa đủ k, ta dừng
            if curr < k:
                break
            
            # tất cả subarrays bắt đầu tại left và kết thúc từ right-1 ... n-1 đều thỏa
            result += n - (right - 1)
            
            # shrink window: loại bỏ arr[left]
            curr -= arr[left]
        
        return result
