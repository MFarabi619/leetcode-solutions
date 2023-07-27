# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#         for i in range(len(head)):
#             currentIndex = i

#             while currentIndex > 0 and head[currentIndex] < head[currentIndex-1]:
#                 head[currentIndex], head[currentIndex-1] = head[currentIndex-1], head[currentIndex]
#                 currentIndex -=1
                
#         return head

        dummy = ListNode(0)  # This node will be the head of sorted list
        curr = head  # Pointer for original list

        while curr is not None:
            # At each iteration, we insert an element into the resulting list.
            prev = dummy  # Pointer for sorted list

            # We find a position to insert the current node in the sorted list.
            while prev.next is not None and prev.next.val < curr.val:
                prev = prev.next

            # Insert the current node to the new position in the sorted list.
            next_node = curr.next  # Store the next node in the original list
            curr.next = prev.next  # Link the current node to the sorted list
            prev.next = curr  # Link the previous node in the sorted list to the current node

            # Move to the next node in the original list
            curr = next_node

        return dummy.next






