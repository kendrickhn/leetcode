import heapq

class Solution:
    def maxRemoval(self, nums, queries):
        n, m = len(nums), len(queries)
        
        # 1) Tính cover[i] = total queries bao phủ i
        diff = [0]*(n+1)
        for l, r in queries:
            diff[l] += 1
            diff[r+1] -= 1
        cover = [0]*n
        curr = 0
        for i in range(n):
            curr += diff[i]
            cover[i] = curr
        # Nếu bất kỳ vị trí i có cover[i] < nums[i], không thể zero ⇒ -1
        for i in range(n):
            if cover[i] < nums[i]:
                return -1
        
        # 2) Chúng ta tìm MINIMAL SET of queries to KEEP sao cho
        #    mỗi vị trí i được bao phủ >= nums[i] lần.
        #    Removed = m - kept.
        
        # Sắp queries theo l tăng dần
        intervals = sorted(queries, key=lambda x: x[0])
        # max-heap lưu các interval active theo r lớn nhất
        max_heap = []
        kept = 0
        
        diff_keep = [0]*(n+1)  # difference array cho số query kept
        curr_kept = 0           # số query kept phủ lên i
        
        ptr = 0
        for i in range(n):
            # 2a) Cập nhật curr_kept từ diff_keep
            curr_kept += diff_keep[i]
            
            # 2b) Đưa vào heap mọi interval bắt đầu tại hoặc trước i
            while ptr < m and intervals[ptr][0] <= i:
                l, r = intervals[ptr]
                # dùng -r để biến thành max‐heap
                heapq.heappush(max_heap, (-r, l, r))
                ptr += 1
            
            # 2c) Loại bỏ khỏi heap những interval không còn active (r < i)
            while max_heap and max_heap[0][2] < i:
                heapq.heappop(max_heap)
            
            # 2d) Nếu curr_kept < nums[i], phải keep thêm
            while curr_kept < nums[i]:
                if not max_heap:
                    return -1  # không còn interval nào để giữ, thất bại
                neg_r, l, r = heapq.heappop(max_heap)
                # keep interval (l,r)
                kept += 1
                curr_kept += 1
                # cập nhật diff_keep để interval này phủ [l..r]
                diff_keep[l] += 1
                diff_keep[r+1] -= 1
            
            # tiếp tục sang i+1 ...
        
        # 3) Kết quả = số queries có thể remove = m - kept
        return m - kept
