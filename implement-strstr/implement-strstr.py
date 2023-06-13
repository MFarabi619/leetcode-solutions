class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # Return the first occurence of the needle string within the haystack string. Don't use the built-in python function to search for a substring, do it manually.

        # If the length of haystack is less than needle, return -1
        if len(haystack)<len(needle): return -1

        # Use two pointers. Loop through haystack, see if the current index matches the first letter. If so, expect the next index to match the next letter. 

        needlePtr = 0

        for haystackPtr, char in enumerate(haystack):

            # Okay attempt #2. A regular brute force solution using two for loops would yield a time complexity of O(n*m), and space complexity of O(1).
            # We have to use some kind of string searching algorithm. Let's go with Knuth-Morris-Pratt (KMP).
            
            # An empty string is not a case that we will come across, so we won't worry about it.

            # lps means 'Longest Prefix Suffix'
            LPS = [0]* len(needle) 

            # Keep track of the previous LPS, and use an i pointer to traverse the needle
            prevLPS, i = 0, 1

            while i < len(needle):
                if needle[i] == needle[prevLPS]:
                    LPS[i]= prevLPS +1
                    prevLPS +=1
                    i+=1 
                
                elif prevLPS == 0:
                        LPS[i]=0
                        i+=1
                else: 
                        prevLPS = LPS[prevLPS-1]
            
            i = 0 # ptr for haystack
            j = 0 # pts for needle
            while i < len(haystack):
                if haystack[i] == needle[j]:
                    i, j = i+1,j+1
                else:
                    if j ==0:
                        i +=1
                    else:
                        j = LPS[j-1]
                if j == len(needle):
                     return i-len(needle)

            return -1
