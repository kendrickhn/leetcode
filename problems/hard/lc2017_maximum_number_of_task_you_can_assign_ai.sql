from bisect import bisect_left

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def can_do(k):
            arr = workers[:]  # copy danh sách công nhân
            pills_left = pills
            for req in reversed(tasks[:k]):
                if arr and arr[-1] >= req:
                    arr.pop()
                else:
                    if pills_left == 0:
                        return False
                    # tìm vị trí công nhân nhỏ nhất có thể +pill đạt req
                    idx = bisect_left(arr, req - strength)
                    if idx == len(arr):
                        return False
                    arr.pop(idx)
                    pills_left -= 1
            return True

        left, right = 0, min(len(tasks), len(workers))
        while left < right:
            mid = (left + right + 1) // 2
            if can_do(mid):
                left = mid
            else:
                right = mid - 1

        return left
