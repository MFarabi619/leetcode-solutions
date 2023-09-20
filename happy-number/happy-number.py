class Solution:
    def isHappy(self, n: int) -> bool:
        # We need to convert n to a string, convert each character back to a digit and square it in order to be able to come up with the final number.
        # n can be many digits. If one number is 1, and the rest are 0, that is the only case where the final result will stay at 1. 
        # I've run some tests using a variety of numbers and the final result is always either 1 or 4. If it's 4, it will never reach 1.

        numString = str(n)

        while True:
            num = sum([int(x) ** 2 for x in numString])
            numString = str(num)
            
            if num == 1:
                return True
            elif num == 4:
                return False
        
        
        