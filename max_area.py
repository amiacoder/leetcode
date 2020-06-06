class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # (end - start) * min(height[end], height[start])
        most_water = 0
        start = 0
        end = len(height) - 1
        while start <= end:
            most_water = max(most_water, (end - start) * min(height[end], height[start]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1 
        return most_water

