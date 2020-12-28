class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = []
        sorted_nums = nums.copy()
        sorted_nums.sort()
        
        i = len(sorted_nums) - 2
        aux_len = sorted_nums[len(sorted_nums) - 1]
        aux = [None for i in range(aux_len + 1)]
        
        while i >= 0:
            if sorted_nums[i] != sorted_nums[i + 1]:
                aux[sorted_nums[i + 1]] = i + 1
            i -= 1
            
        aux[sorted_nums[i + 1]] = 0
        
        answer = []
        i = 0
        for i in range(len(nums)):
            answer.append(aux[nums[i]])
            
        return answer
