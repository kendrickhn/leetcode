from collections import deque
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def compute_depth_parity_counts(n: int, edges: List[List[int]]):
            # Build adjacency list
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            # BFS from node 0 to compute depth parity
            depth = [None] * n
            q = deque([0])
            depth[0] = 0
            c0 = 1  # count of nodes at even depth
            c1 = 0  # count at odd depth
            while q:
                u = q.popleft()
                for w in adj[u]:
                    if depth[w] is None:
                        depth[w] = depth[u] + 1
                        if depth[w] % 2 == 0:
                            c0 += 1
                        else:
                            c1 += 1
                        q.append(w)
            return depth, c0, c1

        n1 = max(max(u, v) for u, v in edges1) + 1 if edges1 else 1
        n2 = max(max(u, v) for u, v in edges2) + 1 if edges2 else 1

        # Compute for tree1
        depth1, c0_1, c1_1 = compute_depth_parity_counts(n1, edges1)
        # Compute for tree2
        depth2, c0_2, c1_2 = compute_depth_parity_counts(n2, edges2)
        best2 = max(c0_2, c1_2)

        # Build answer for each node i in tree1
        ans = [0] * n1
        for i in range(n1):
            if depth1[i] % 2 == 0:
                even1 = c0_1
            else:
                even1 = c1_1
            ans[i] = even1 + best2

        return ans
