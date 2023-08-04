class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        n = len(nums[0])
        for k, trim in queries:
            trimmed = [(int(num[n-trim:]), i) for i, num in enumerate(nums)]
            _, i = sorted(trimmed, key=lambda x: [x[0], x[1]])[k-1]
            ans.append(i)
        return ans


