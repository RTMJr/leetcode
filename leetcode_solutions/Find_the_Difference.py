class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = collections.Counter(s)
        count_t = collections.Counter(t)
        
        answer = ""
        for ch in t:
            if (ch not in count_s) or (count_s[ch] != count_t[ch]):
                answer += ch
                break
        
        return answer
        
