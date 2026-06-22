class Solution(object):
    def maxSubArray(self, nums):
        current_sum = 0
        minimum_sum = float("-inf")

        for i in range(0, len(nums)):
            current_sum = max(nums[i], nums[i] + current_sum)
            minimum_sum = max(minimum_sum, current_sum)

        return minimum_sum