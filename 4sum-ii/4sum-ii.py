class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Create the hashmap for sums of A and B
        sum_map = {}
        for a in nums1:
            for b in nums2:
                # Increment the count of their sum
                sum_map[a + b] = sum_map.get(a + b, 0) + 1

        # Initialize the counter
        count = 0

        # Check for valid tuples using C and D
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in sum_map:
                    count += sum_map[target]

        # Return the final count
        return count