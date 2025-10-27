import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        deleted = [False] * len(s)
        
        for i, char in enumerate(s):
            if char == '*':
                if heap:
                    # The heap stores (char, -index) to prioritize the smallest char and the rightmost if duplicates
                    val, neg_idx = heapq.heappop(heap)
                    deleted[-neg_idx] = True
            else:
                heapq.heappush(heap, (char, -i))
        
        result = []
        for i, char in enumerate(s):
            if char != '*' and not deleted[i]:
                result.append(char)
        
        return ''.join(result)