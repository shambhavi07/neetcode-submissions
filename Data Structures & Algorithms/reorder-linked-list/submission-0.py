# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle
        slow,fast=head,head
        # we have to go until the fast.next is none i.e. boundary reached
        # Time: O(n)
        while fast and fast.next:
            slow= slow.next
            fast=fast.next.next

        # reverse the second half
        # startSec= starting val for second half mof the list
        second= slow.next
        # cut the list by putting a none so prev pointer can be used
        slow.next=None
        prev=None
        # we revesre until we reach the end
        # Time: O(n/2)
        while second:
            nxt= second.next #save
            second.next=prev #flip
            prev=second #move prev
            second=nxt #move second
        
        # merge the lists
        first, second= head, prev
        while second:
            tmp1, tmp2= first.next, second.next
            first.next= second
            second.next= tmp1
            first=tmp1
            second=tmp2
            
            

