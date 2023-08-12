# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # We can traverse both linkes lists and return if the node of one linked list equals the other

        if headA and headB:
            A, B = headA, headB
            
        while A is not B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
