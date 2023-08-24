# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointerA = head
        pointerB = head

        while pointerB and pointerB.next:
            pointerA = pointerA.next
            pointerB = pointerB.next.next

        return pointerA
