class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Convert the string into an array.  
        stringArr = list(s)

        # Loop throught the array until the first space is found, reverse everything behind the space. Continue until the end of the array is reached. 
        wordStart = 0

        for i, char in enumerate(stringArr):
            if char==' ' or i==len(stringArr)-1:
                if i==len(stringArr)-1:
                    stringArr[wordStart:i+1] = stringArr[wordStart:i+1][::-1]
                else: stringArr[wordStart:i] = stringArr[wordStart:i][::-1]
                wordStart = i+1

        return ''.join(stringArr)