class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        answer = 0
        left = 0
        right = len(mat) - 1
        for i in range(len(mat)):
            answer += mat[i][left]
            answer += mat[i][right]
            if (left == right):
                answer -= mat[i][left]
            left += 1
            right -= 1
            
            
        return answer
