tion for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start = -n + 1
        end_node = head
        start_node = head
        pre_node = None
        while end_node.next:
            end_node = end_node.next
            start += 1
            if start > 0:
                pre_node = start_node
                start_node = start_node.next
        if not pre_node:
            return head.next
        pre_node.next = start_node.next
        return head
