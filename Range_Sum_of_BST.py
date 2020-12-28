class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def in_order(root):
            if (root == None):
                return 0
            nonlocal total
            in_order(root.left)
            if ((root.val >= low) and (root.val <= high)):
                total += root.val
            in_order(root.right)
            
        total = 0
        in_order(root)
        return total
