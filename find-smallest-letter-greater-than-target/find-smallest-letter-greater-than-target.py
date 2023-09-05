class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # If we can assign a numeric value to the letter, we can use binary search. Since the array is already sorted in non-decreasing order.
        
        left = 0
        right = len(letters) - 1
    
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        if left == len(letters):
            return letters[0]
        else:
            return letters[left]