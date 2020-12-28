class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        words_a, words_b = A.split(), B.split()
        dict_a, dict_b = collections.Counter(words_a), collections.Counter(words_b)
        
        answer = []
        for key in dict_a:
            if (dict_a[key] == 1) and (key not in dict_b):
                answer.append(key)
        
        for key in dict_b:
            if (dict_b[key] == 1) and (key not in dict_a):
                answer.append(key)
        
        return answer
