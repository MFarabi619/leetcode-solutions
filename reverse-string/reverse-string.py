class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        # We can use two pointers, one from the start and one from the end. We simply swap the element contained in each pointer.

        a = 0
        b=len(s)-1

        while a<b:
            s[a], s[b]=s[b], s[a]
            a+=1
            b-=1

        return s
