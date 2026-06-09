class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        right= len(arr)-1
        left =0 
        while left<right:
            mid = (left+right) // 2
            if arr[mid] < arr[mid +1]:
                left = mid+1
            else:
                right = mid 
        return left


        