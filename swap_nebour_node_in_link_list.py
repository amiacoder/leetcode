# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        result_head = None
        cursor = head
        next_cursor = cursor.next
        last_node = None
        while cursor and next_cursor:
            # print 'test', cursor.val, next_cursor.val
            temp_cursor = next_cursor.next
            next_cursor.next = cursor
            cursor.next = temp_cursor
            if last_node:
                last_node.next = next_cursor
            last_node = cursor
            if not result_head:
                result_head = next_cursor
            if not cursor.next or not cursor.next.next:
                break
            cursor = cursor.next
            next_cursor = cursor.next
            # print cursor.val, next_cursor.val
        return result_head
