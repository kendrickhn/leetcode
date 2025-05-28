from collections import defaultdict, deque

def bfs_distance(tree, start, max_depth):
    visited = set()
    dist = {}
    q = deque([(start, 0)])
    while q:
        node, d = q.popleft()
        if node in visited or d > max_depth:
            continue
        visited.add(node)
        dist[node] = d
        for nei in tree[node]:
            if nei not in visited:
                q.append((nei, d + 1))
    return dist

class Solution:
    def maxTargetNodes(self, edges1, edges2, k):
        n = len(edges1) + 1
        m = len(edges2) + 1

        # Build both trees
        treeA = defaultdict(list)
        for u, v in edges1:
            treeA[u].append(v)
            treeA[v].append(u)

        treeB = defaultdict(list)
        for u, v in edges2:
            treeB[u].append(v)
            treeB[v].append(u)

        # Precompute distances for all Tree B nodes (only once)
        treeB_reach = []
        for j in range(m):
            distB = bfs_distance(treeB, j, k - 1)  # Only up to distance k - 1
            treeB_reach.append(len(distB))

        res = []
        for i in range(n):
            distA = bfs_distance(treeA, i, k)
            countA = len(distA)
            max_total = 0
            for b_count in treeB_reach:
                total = countA + b_count  # disjoint sets
                max_total = max(max_total, total)
            res.append(max_total)
        return res
