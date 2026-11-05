# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while h1 and h2:
            if h1.val < h2.val:
                tail.next = h1
                h1 = h1.next
            else:
                tail.next = h2
                h2 = h2.next
            tail = tail.next

        if h1:
            tail.next = h1
        if h2:
            tail.next = h2

        return dummy.next
