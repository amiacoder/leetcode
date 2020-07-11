class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) / 2
            # print start, end, mid
            if target == nums[mid]:
                return mid
            if nums[start] <= nums[mid]:
                if target >= nums[start] and target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target >= nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
