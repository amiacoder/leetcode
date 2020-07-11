class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 1:
            return [-1, -1]
        start = 0
        end = len(nums) - 1
        result = [-1, -1]
        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                des_start = mid
                des_end = mid
                while des_start >= start:
                    if nums[des_start] == target:
                        result[0] = des_start
                        des_start -= 1
                    else:
                        break
                while des_end <= end:
                    if nums[des_end] == target:
                        result[1] = des_end
                        des_end += 1
                    else:
                        break
                return result
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
            
        return [-1, -1]
