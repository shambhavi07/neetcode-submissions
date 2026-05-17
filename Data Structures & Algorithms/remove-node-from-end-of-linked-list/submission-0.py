# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy= ListNode(0, head)
        fast=slow=dummy
        # now we move fast by N+1 then mv slow and contiinue moiving fast
        for _ in range(n+1):
            fast= fast.next
        # while every fast pointer at correct gap mv slow 
        while fast:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummy.next
        