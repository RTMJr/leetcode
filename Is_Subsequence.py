class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if (len(s) == 0):
            return True
        
        pointer1 = 0
        pointer2 = 0
        while (pointer1 < len(t) and pointer2 < len(s)):
            if (t[pointer1] == s[pointer2]):
                pointer2 += 1
            pointer1 += 1
            
        return (pointer2 == len(s))
