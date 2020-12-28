lass Solution:
    def deleteNode(self, node):
        while (node):
            node.val = node.next.val
            if (node.next.next == None):
                node.next = None
            node = node.next
