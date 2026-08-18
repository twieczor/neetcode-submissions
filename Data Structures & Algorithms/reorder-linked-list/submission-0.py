# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        l,r = head, head
        first = None
        prev = None

        while l.next is not None and l.next.next is not None:

            while r.next is not None:
                prev = r
                r = r.next

            prev.next = None

            r.next = l.next

            l.next = r

            if first is None:                
                first = l
                print(first.val)
                print(first.next)

            l = l.next.next
        
        #while node.next is not None:
        #    print(node.val)
