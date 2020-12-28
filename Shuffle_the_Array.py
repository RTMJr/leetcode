class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x_index = 0
        y_index = n
        answer = []
        while x_index < n:
            answer.append(nums[x_index])
            answer.append(nums[y_index])
            x_index += 1
            y_index += 1
        return answer
