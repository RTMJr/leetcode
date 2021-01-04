class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(1, len(nums), 2):
            count = nums[i - 1]
            while (count):
                answer.append(nums[i])
                count -= 1
        
        return answer
