class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        shift = min(nums)
        K = max(nums) - shift
        counts = [0] * (K+1)
        for elem in nums:
            counts[elem - shift] += 1

        # Overwrite original counts with the starting index
        # of each element in the final sorted array

        starting_index = 0
        for i,count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count

        sorted_lst = [0] * len(nums)
        for elem in nums:
            sorted_lst[counts[elem-shift]] = elem
            # Since we've plan an item in index counts[elem], we need to increment counts[elem] index by 1 so the next duplicate element is places in appropriate index
            counts[elem - shift] += 1

        # Common practice tocoy over sorted list into original list.
        for i in range(len(nums)):
            nums[i] = sorted_lst[i]
        return nums