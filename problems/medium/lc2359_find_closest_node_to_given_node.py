from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        
        # Helper to compute distance from start to every node reachable
        def get_distances(start):
            dist = [float('inf')] * n
            cur = start
            d = 0
            # Walk following the single outgoing edge until -1 or cycle
            while cur != -1 and dist[cur] == float('inf'):
                dist[cur] = d
                d += 1
                cur = edges[cur]
            return dist
        
        dist1 = get_distances(node1)
        dist2 = get_distances(node2)
        
        # Find node i minimizing max(dist1[i], dist2[i]), tie-breaking on smaller i
        best_node = -1
        best_dist = float('inf')
        for i in range(n):
            d = max(dist1[i], dist2[i])
            if d < best_dist:
                best_dist = d
                best_node = i
        
        return best_node
