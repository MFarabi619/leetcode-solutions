class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # The minimum length of the array is 2.

        # Looking at the examples, I see a pattern.
        # The largest numbers are paired with each other,
        # and vice versa for the smallest numbers. 
        # We can sort the array first, and just generate the pairs.
        # The python sort() function used Timsort under the hood, which has a worst case time complexity of O(nlogn).

        total = 0
        nums = sorted(nums)

        # for index in range(1, len(nums),2):
        #     total += min(nums[index],nums[index-1])
        

        # Instead of taking the minimum between a pair, we know for a fact that the minimum element is going to always be the first number of the pair. So we can just do the following.

        for index in range(0,len(nums),2):
            total+= nums[index]

        return total
