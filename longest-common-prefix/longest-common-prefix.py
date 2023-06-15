class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
         # We can loop through the indices of all strings in the array at the same, this will give us a linear time solution

        # Iterate over all the elements of the string array at the same time.
        # As soon as one letter is found that doesn't match the rest, return the prefix.


        zipped = zip(*strs)
        longestPrefix = 0
        longestPrefixString = ''

        for element in zipped:
            # All letters are the same, so the length of the set is 1
            if len(set(element)) ==1: 
                longestPrefixString+= str(next(iter(set(element))))

            else:
                return longestPrefixString

        return longestPrefixString 