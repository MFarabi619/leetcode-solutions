class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
                
        # There's always exactly one solution. The length of numbers array will always be at least two.

        # Begin the loop from the first element of the array. Look for a number that is target-currentNum. 

        # Any number that is greater than the target cannot add up to targetNum and can be ignored. So we find the first number in the array that is less than or equal to target. The rest of the array doesn't have to be searched. 
        
        # Another optimization can be made. If the smallest number and the largest number add up to more than target, the largest number can just be removed. Because any number greater than the smallest number added to the largest number would also add up to greater than target.

        i , j = 0, len(numbers)-1
        while i < j:
            sum = numbers[i]+numbers[j]
            if sum==target:
                return [i+1,j+1]
            elif sum>target:
                j-=1
            else:
                i+=1
