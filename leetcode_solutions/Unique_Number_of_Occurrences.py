class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        table = {}
        for a in arr:
            table[a] = 0
        
        for a in arr:
            table[a] += 1
        
        s = set()
        for key, value in table.items():
            if value in s:
                return False
            else:
                s.add(value)
        
        return True
