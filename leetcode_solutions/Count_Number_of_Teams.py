class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0
        
        answer = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                for k in range(j + 1, len(rating)):
                    if rating[i] < rating[j] and rating[j] < rating[k]:
                        answer += 1
                    if rating[i] > rating[j] and rating[j] > rating[k]:
                        answer += 1
                        
        return answer
