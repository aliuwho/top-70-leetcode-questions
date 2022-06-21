class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i in range(len(nums)):
            complement = str(target - nums[i])
            if complement in seen.keys():
                return [i, seen[complement]]
            else:
                seen[str(nums[i])] = i