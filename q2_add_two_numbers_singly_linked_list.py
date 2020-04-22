#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        place_iter = dummy_head = ListNode()
        carry = 0
        while l1 or l2 or carry:
            data = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            place_iter.next = ListNode(data % 10)
            carry, place_iter = data // 10, place_iter.next
        return dummy_head.next
            
