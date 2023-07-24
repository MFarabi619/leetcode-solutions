class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """ 

        # We can take each word in the string, add them to another array, and then reverse the array.
        # Strings are immutable in python, so we can't achieve an O(1) solution.
        # In a language where strings are mutable, the process would remain very similar. You can use a two-pointer approach to reverse the string in-place.

        stringArr = []

        # Add each character of the string to an array in reverse order
        def reverse(s):
            i = len(s)-1
            while i>=0:
                stringArr.append(s[i])
                i -=1
        
        # Clean up spaces within the string array
        def cleanSpaces(stringArr):
            length = len(stringArr)
            i, j = 0, 0

            while (j < length):
                while (j < length and stringArr[j] == ' '): j+=1
                while (j < length and stringArr[j] != ' '): 
                    stringArr[i]=stringArr[j]
                    i+=1
                    j+=1
                while (j < length and stringArr[j] == ' '): j+=1
                if (j < length): 
                    stringArr[i] = ' '
                    i+=1

            return stringArr[:i]
        
        reverse(s)
        stringArr = cleanSpaces(stringArr)

        wordStartIndex = 0

        for i, char in enumerate(stringArr):
            if char == ' ' or i==len(stringArr)-1:
                if char !=' ':
                    i+=1
                stringArr[wordStartIndex:i] = stringArr[wordStartIndex:i][::-1]
                wordStartIndex = i+1
        
        return ''.join(stringArr)
