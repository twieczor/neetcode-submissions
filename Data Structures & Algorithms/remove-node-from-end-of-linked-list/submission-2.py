# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head is None:
            return
        if head.next is None:
            head = None
            return

        prev,l,r = head,head,head

        while r is not None:
            r = r.next
            if n > 0:
                n -= 1
            else:
                prev = l
                l = l.next

        print(prev.val, l.val)

        if prev != l:
            prev.next = l.next
        else:
            head = head.next

        return head




