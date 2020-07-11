class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return -1
        if target > nums[-1]:
            # 正序
            destination = -1
            i = 0
            while target > nums[i] and i < len(nums) - 2:
                if target == nums[i]:
                    destination = i
                    break
                if nums[i+1] < nums[i]:
                    break
                i += 1
            if target == nums[i]:
                destination = i
            return destination
        elif target < nums[-1]:
            # 倒序
            destination = -1
            i = len(nums) - 1
            while target < nums[i] and i > 0:
                if target == nums[i]:
                    destination = i
                    break
                if nums[i-1] > nums[i]:
                    break
                i -= 1
            if target == nums[i]:
                destination = i
            return destination
        else:
            return len(nums) - 1
