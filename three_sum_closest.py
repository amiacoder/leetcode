class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = None
        gap = None
        for i in range(0, len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            if not gap:
                gap = abs(target-nums[i]-nums[left]-nums[right])
                result = nums[i] + nums[left] + nums[right]
            while left < right:
                if abs(target-nums[i]-nums[left]-nums[right]) < gap:
                    gap = abs(target-nums[i]-nums[left]-nums[right])
                    result = nums[i] + nums[left] + nums[right]
                if nums[left] + nums[right] > target - nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < target - nums[i]:
                    left += 1
                else:
                    return target
        return result






