class Solution(object):
    def getRow(self, rowIndex):
        """"
        :type rowIndex: int
        :rtype: List[int]
        """

        # There are multiple ways to solve this problem. One approach is to find all the previous rows in order to get to current row. This can be done iteratively or recursively. However is there a mathematical formula that we can use to find the current row? This would require less code and be more 'elegant'

        # Yes we can. We can use a mathematical formula that can find any row of Pascal's triangle. The formula is known as the binomial coefficient theorem.
        # The binomial coefficient formula is:
        # C(n,k) n!/(k!*(n-k)!) 
        # where n is the row number and k is the position of the number in that row.

        # nC0 = 1
        prev = 1

        numArray = [1]
    
        for i in range(1, rowIndex + 1):
    
        #   C(n,k) n!/(k!*(n-k)!)  
            curr = (prev * (rowIndex - i + 1)) // i
            numArray.append(curr)
            prev = curr

        return numArray