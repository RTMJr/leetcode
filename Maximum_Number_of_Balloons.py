class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = collections.Counter(text)
        count_balloon = collections.Counter('balloon')
        return min([count[c] // count_balloon[c] for c in count_balloon])
