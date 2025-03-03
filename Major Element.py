class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        n = len(nums)
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
            if counts[i] > n//2:
                return i
