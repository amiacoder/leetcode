# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            elif root1 and root2:
                return (root1.val == root2.val) and dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
            elif root1 or root2:
                return False
        return dfs(root.left, root.right)


        
