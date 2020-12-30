class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = [-1, -1]
        first = False
        for idx, val in enumerate(nums):
            if first and val == target:
                answer[1] = idx
            if not first and val == target:
                first = True
                answer[0] = idx
        
        if first and answer[1] == -1:
            answer[1] = answer[0]
                
        return answer
