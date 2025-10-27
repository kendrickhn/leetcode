import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        INF = 10**30
        
        # dist[i][j][p]: earliest time to reach (i,j) with parity p
        # p = 0 means next move will cost 1s, p = 1 means next move will cost 2s
        dist = [[[INF, INF] for _ in range(m)] for _ in range(n)]
        dist[0][0][0] = 0
        
        # Min-heap of (time, i, j, parity)
        pq = [(0, 0, 0, 0)]
        dirs = ((1,0),(-1,0),(0,1),(0,-1))
        
        while pq:
            t, i, j, p = heapq.heappop(pq)
            if t > dist[i][j][p]:
                continue
            # Once we pop the target, it's the global minimum
            if i == n-1 and j == m-1:
                return t
            
            # Explore neighbors
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    # cost alternates: 1s if p==0, else 2s
                    cost = 1 if p == 0 else 2
                    # cannot start moving into (ni,nj) before its moveTime
                    start = max(t, moveTime[ni][nj])
                    nt = start + cost
                    np = 1 - p
                    if nt < dist[ni][nj][np]:
                        dist[ni][nj][np] = nt
                        heapq.heappush(pq, (nt, ni, nj, np))
        
        # If unreachable (shouldn't happen per problem statement)
        return -1