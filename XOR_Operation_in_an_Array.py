class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        if n == 1:
            return start
        nums = []
        for i in range(n):
            nums.append(start + (2*i))
            
        answer = nums[0]
        for i in range(1, len(nums)):
            answer ^= nums[i]
        
        return answer
