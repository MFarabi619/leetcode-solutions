class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        # Remove all occurences of integer val from nums in-place
        # Return the number of elements in nums which are not equal to val
        # All values not equal to val must be shifted forward such that they are at the beginning of the array.

        #1: Loop through the array, if element at index equals val, add to k.
        #2: Remove element at index.

         
        k = len(nums)

        for i in range(0,len(nums)):
            while (nums[i]==val):
                k-=1 
                nums.pop(i)
                nums.append('')
        
        return k 