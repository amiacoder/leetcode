# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

result = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def current_branch_contains_destination(node, p, q):
            if not node:
                return False
            global result
            left_result = current_branch_contains_destination(node.left, p, q)
            right_result = current_branch_contains_destination(node.right, p, q)
            if node.val == p.val or node.val == q.val:
                if left_result or right_result:
                    result = node
                return True
            if left_result and right_result:
                result = node
                return True
            if left_result or right_result:
                return True
        current_branch_contains_destination(root, p, q)
        return result

