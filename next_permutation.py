class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return None
        left = len(nums) - 2
        right = len(nums) - 1
        while left >= 0:
            if nums[right] > nums[left]:
                break
            else:
                right -= 1
                left -= 1
        i = len(nums) - 1

        while i >= right:
            if nums[i] > nums[left]:
                temp = nums[left]
                nums[left] = nums[i]
                nums[i] = temp
                break
            i -= 1
        right_arr = nums[right:len(nums)]
        right_arr.sort()
        i = right
        while i < len(nums):
            nums[i] = right_arr[i-right]
            i += 1
        return nums

        
