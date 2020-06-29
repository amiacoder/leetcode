class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        print nums
        result = []
        for i in range(0, len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                # print 'test', i, j, left, right
                while left < right:
                    # print i, j, left, right
                    if left > j + 1 and nums[left] == nums[left-1]:
                        left += 1
                        continue
                    if right < len(nums) - 1 and nums[right] == nums[right+1]:
                        right -= 1
                        continue
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        left += 1
        return result
