class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        second = False
        first = False
        a = 0
        start = nums[0]
        while a < len(nums):
            if nums[a] > start and first == False: 
                first = True
                start2 = nums[a]
                a += 1 
            elif first == True and nums[a] > start2: 
                return True
            elif first == True and nums[a] <= start2 and nums[a] > start:
                start2 = nums[a]
                a += 1
            elif first == True and nums[a] < start: 
                start = nums[a]
                a += 1
            elif first == False and nums[a] < start: 
                start = nums[a]
                a += 1
            else: 
                a += 1
        return second
