class Solution(object):
    def maxProduct(self, nums):
        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]

        for i in range (1,len(nums)):
            x = nums[i]
            if x < 0:
                curr_max,curr_min = curr_min,curr_max
            curr_max = max(x,curr_max*x)
            curr_min = min(x,curr_min*x)
            result = max(result,curr_max)
        return result