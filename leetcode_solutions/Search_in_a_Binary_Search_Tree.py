class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return None
        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)
        return root
