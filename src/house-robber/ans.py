class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        # case where we have >= 3 houses:
        maxes = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            currMax = max(maxes[1], maxes[0] + nums[i])
            maxes[0] = maxes[1]
            maxes[1] = currMax
        return currMax