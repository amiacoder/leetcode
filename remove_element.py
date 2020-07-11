class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        result = 0
        none_index = []
        while i < len(nums):
            if nums[i] == val:
                nums[i] = None
                none_index.append(i)
            else:
                if len(none_index) > 0:
                    nums[none_index[0]] = nums[i]
                    nums[i] = None
                    none_index = none_index[1:]
                    none_index.append(i)
                result = i - len(none_index) + 1
            i += 1
        return result
        
