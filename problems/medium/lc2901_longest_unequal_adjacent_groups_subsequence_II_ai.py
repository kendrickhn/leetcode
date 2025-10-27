from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        
        # Kiểm tra xem có thể nối j → i không
        def can_connect(j: int, i: int) -> bool:
            if groups[j] == groups[i]:
                return False
            wj, wi = words[j], words[i]
            if len(wj) != len(wi):
                return False
            diff = 0
            for x, y in zip(wj, wi):
                if x != y:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        
        dp = [1] * n
        prev = [-1] * n
        
        # Tính dp[i] = độ dài dài nhất kết thúc tại i
        for i in range(n):
            for j in range(i):
                if can_connect(j, i) and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        
        # Tìm điểm kết thúc tốt nhất
        end = max(range(n), key=lambda i: dp[i])
        
        # Khôi phục dãy chỉ số
        seq = []
        cur = end
        while cur != -1:
            seq.append(cur)
            cur = prev[cur]
        seq.reverse()
        
        # Trả về các từ tương ứng
        return [words[i] for i in seq]
