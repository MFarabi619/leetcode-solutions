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
        """
        We can use a hashmap to keep track of nodes already copied. Do a first pass over the list to copy the nodes, and then a second pass to copy the next and random pointers.
        
        I was unable to come up with an efficient solution, this is from NeetCode.
        """
        
        oldToCopy = {None:None}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
            
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
            
        return oldToCopy[head]