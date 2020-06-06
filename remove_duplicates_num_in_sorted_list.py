class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = len(nums) - 1
        last_value = None
        while index >= 0:
            if last_value != None and nums[index] == last_value:
                del(nums[index])
            else:
                last_value = nums[index]
            index -= 1
        return len(nums)
