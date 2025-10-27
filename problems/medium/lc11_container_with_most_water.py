class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        if len(height) < 2: 
            return max    
        a = 0
        b = len(height)-1
        
        while a != b: 
            if height[b] >= height[a]:
                contain = height[a]*(b-a)
                if contain > max: 
                    max = contain
                a += 1
            elif height[a] > height[b]: 
                contain = height[b]*(b-a)
                if contain > max: 
                    max = contain
                b -= 1
        return max