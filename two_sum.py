class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp_dict = {}
        i = 0
        while i < len(nums):
            item = nums[i]
            if target-item in temp_dict and temp_dict[target-item] != None:
                return [temp_dict[target-item], i]
            else:
                temp_dict[item] = i
            i += 1
        return []
