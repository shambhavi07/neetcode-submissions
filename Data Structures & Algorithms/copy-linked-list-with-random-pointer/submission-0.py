"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        #   none->none to handle null pointers
        old_to_new= {None: None}

        # pass 1: get the old to new mapping
        # curr holds the address and we get value at this adress by curr.val
        curr=head
        while curr:
            old_to_new[curr]= Node(curr.val) #Node() calls the contructure from the Node class in the problem defination to create a new node
            curr=curr.next
        # pass2: to wire next and random
        curr=head
        while curr:
            # set the copy's next pointer 
            #  to point at 
            #  the copy of the original's next node
            old_to_new[curr].next= old_to_new[curr.next]
            old_to_new[curr].random= old_to_new[curr.random]
            curr= curr.next
        return old_to_new[head]
