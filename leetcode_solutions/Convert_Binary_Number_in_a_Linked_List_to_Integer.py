class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        current = head
        digits = -1
        while current:
            digits += 1
            current = current.next
            
        answer = 0
        current = head
        while current:
            if current.val == 1:
                result = int(math.pow(2.0, digits))
                answer += result
            digits -= 1
            current = current.next
        
        return answer
