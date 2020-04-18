# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        cnode = None
        while l1 != None and l2 !=None:
            tmp_node = None
            if l1.val < l2.val:
                 tmp_node = l1
                 l1 = l1.next
            else:
                tmp_node = l2
                l2 = l2.next
            if head is None:
                head = tmp_node
            if cnode is not None:
                cnode.next = tmp_node;
            cnode = tmp_node

        if l1 is None:
            if cnode is None:
                cnode = l2
                head = cnode
            else:
                cnode.next = l2
        else:
            if cnode is None:
                cnode = l1
                head = cnode
            else:
                cnode.next = l1
        return head

