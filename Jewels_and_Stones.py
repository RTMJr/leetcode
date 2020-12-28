class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        table = {}
        for i in range(len(S)):
            table[S[i]] = False
        
        for i in range(len(J)):
            table[J[i]] = True
        
        answer = 0
        for i in range(len(S)):
            if (table[S[i]]):
                answer += 1
        
        return answer
