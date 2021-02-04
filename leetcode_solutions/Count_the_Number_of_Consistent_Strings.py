class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)
        
        total = len(words)
        for w in words:
            not_allowed = False
            for i in w:
                if i not in s:
                    total -= 1
                    not_allowed = True
                if not_allowed:
                    break
        
        return total
