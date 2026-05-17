# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0, head)
        prev = dummy

        while True:
            # check if k nodes exists                                  
            check = prev
            for _ in range(k):
                check=check.next
                if check is None:
                    return dummy.next
            # group boundries
            curr=prev.next
            group_next=check.next

            # reverse
            p=None
            c=curr
            for _ in range(k):
                nxt=c.next
                c.next=p
                p=c
                c=nxt

            # reconnect
            prev.next=p
            curr.next=group_next
            prev=curr