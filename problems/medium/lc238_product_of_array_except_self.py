# solved in 22:52
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        answer = []
        if 0 not in nums: 
            for i in nums: 
                total = total * i
            for i in nums: 
                answer.append(int(total/i))
        
        else: 
            a = nums.count(0)
            if a >= 2: 
                for i in nums: 
                    answer.append(0)
            else:
                for i in nums: 
                    if i != 0: 
                        total = total * i
                for i in nums: 
                    if i != 0: 
                        answer.append(0)
                    else: 
                        answer.append(total)
        return answer
        