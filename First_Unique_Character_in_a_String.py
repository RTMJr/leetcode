class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_s = collections.Counter(s)
        for i in range(len(s)):
            if (count_s[s[i]] == 1):
                return i
        
        return -1
