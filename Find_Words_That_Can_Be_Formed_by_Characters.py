class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        answer, count_of_chars = 0, collections.Counter(chars)
        for w in words:
            chars_in_str = True
            word_chars_count = collections.Counter(w)
            for ch in w:
                if word_chars_count[ch] > count_of_chars[ch]:
                    chars_in_str = False
                    break
            if chars_in_str:
                answer += len(w)
        
        return answer
                
