class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.quick_sort(nums)

    def quick_sort(self, nums):
        n = len(nums)
        def quick(left, right):
            if left >= right:
                return nums
            pivot = left
            i = left
            j = right
            while i < j:
                while i < j and nums[j] > nums[pivot]:
                    j -= 1
                while i < j and nums[i] <= nums[pivot]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[pivot], nums[j] = nums[j], nums[pivot]
            quick(left, j - 1)
            quick(j + 1, right)
            return nums
        return quick(0, n - 1)

