class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
            
        middle = (count // 2) + 1
        middle_node = None
        current = head
        count = 0
        while current:
            count += 1
            if count == middle:
                middle_node = current
                break
            current = current.next
        
        return middle_node
