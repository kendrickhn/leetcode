# solved in 26:30
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        avail = 0
        cap = len(flowerbed)
        if len(flowerbed) > 2:
            for i in range(cap): 
                if i == 0 and flowerbed[i] + flowerbed[i+1] == 0:
                    avail += 1
                    flowerbed[i] += 1
                elif i == len(flowerbed) - 1 and flowerbed[i] + flowerbed[i-1] == 0:
                    avail += 1
                    flowerbed[i] += 1
                elif i != 0  and i != cap -1 and flowerbed[i] == 0 and flowerbed[i+1] + flowerbed[i-1] == 0:
                    avail += 1
                    flowerbed[i] += 1
        else: 
            if 1 not in flowerbed: 
                avail += 1
        return avail >= n



