from .list_node import ListNode

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        copy_l1 = l1
        copy_l2 = l2
        ret = ListNode(0)
        tmp = ret
        while copy_l1 or copy_l2:
            val_l1 = copy_l1.val if copy_l1 else 0
            val_l2 = copy_l2.val if copy_l2 else 0

            tmp.val = val_l1 + val_l2 + tmp.val

            next_node_init_value = 0
            if tmp.val >= 10:
                tmp.val = tmp.val - 10
                next_node_init_value = 1

            if copy_l1:
                copy_l1 = copy_l1.next

            if copy_l2:
                copy_l2 = copy_l2.next

            if copy_l1 or copy_l2 or next_node_init_value > 0:
                tmp.next = ListNode(next_node_init_value)

            tmp = tmp.next

        return ret
