# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = 0
        f_n = 0
        while l1:
            f_n += l1.val * 10 ** i
            i += 1
            l1 = l1.next

        j = 0
        s_n = 0
        while l2:
            s_n += l2.val * 10 ** j
            j += 1
            l2 = l2.next
        
        sum_ =  f_n + s_n
        
        if sum_ == 0:
            return ListNode(0)

        head = ListNode(-1)
        node = head
        while sum_ > 0:
            t = sum_ % 10
            node.next = ListNode(t)
            node = node.next
            sum_ = sum_ // 10
        
        return head.next



