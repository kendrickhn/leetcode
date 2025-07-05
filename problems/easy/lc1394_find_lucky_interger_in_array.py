class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a = -1
        for i in arr: 
            if arr.count(i) == i and i > a: 
                a = i 
        return a 
