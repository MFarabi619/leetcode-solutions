# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        # Step 1: Calculate the length of the linked list
        length = 1
        temp = head
        while temp.next:
            length += 1
            temp = temp.next
        
        # Step 2: Modify the value of k
        k %= length
        
        # If k is 0, just return the head
        if k == 0:
            return head
        
        # Step 3: Use the two-pointer approach
        ptr1 = head
        for _ in range(k):
            ptr1 = ptr1.next
        
        ptr2 = head
        while ptr1.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        # Step 4: Rearrange the linked list
        temp = ptr2.next
        ptr2.next = None
        ptr1.next = head
        head = temp
        
        return head
