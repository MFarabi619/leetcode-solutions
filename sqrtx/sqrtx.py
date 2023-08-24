class Solution:
    def mySqrt(self, x: int) -> int:
        """
        We can create an array going up to 1/2 of the integer.
        This is because the square root of a number is guranteed to be less than half of the number for any value above 4. 
        """
        if x <= 1:
            return x
        mid, left, right = 0, 1, x//2
        
        while True:
            mid = (left + right)//2
            if mid > 0 and mid > x//mid:
                right = mid -1 
            elif mid + 1 > x // (mid+1):
                return mid
            else: left = mid + 1
            
        
        
        
        