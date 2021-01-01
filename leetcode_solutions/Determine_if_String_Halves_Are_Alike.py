class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiou")
        
        s = s.lower()
        s = list(s)
        mid = len(s) // 2
        left_count = 0
        right_count = 0
        for char in s[:mid]:
            if char in vowels:
                left_count += 1
                
        for char in s[mid:]:
            if char in vowels:
                right_count += 1
                
        return left_count == right_count
