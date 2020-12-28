class Solution:
    def __init__(self):
        self.new_root = TreeNode()
        self.curr = self.new_root
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def in_order(root):
            if root:
                in_order(root.left)
                self.curr.right = TreeNode(val=root.val)
                self.curr = self.curr.right
                in_order(root.right)
                
        in_order(root)        
                
        return self.new_root.right
