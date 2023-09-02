class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # The property of nums[i] != nums[i + 1] for all valid i pretty much gurantees that a peak must exist in the array.
        # We look to both sides of the mid pointer, and always move to the greater number side. Once we hit a lesser number or the edge of the array, we've found our peak.
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Left number is greater
            if mid > 0 and nums[mid] < nums[mid - 1]:
                right = mid - 1
                
            # Right number is greater
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                left = mid + 1
                
            else:
                return mid
                
        
            