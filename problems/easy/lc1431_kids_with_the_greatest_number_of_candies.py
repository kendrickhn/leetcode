# solved in 9:40
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxc = max(candies)
        results = []
        for i in candies:
                results.append(i + extraCandies >= maxc)
        return results
        