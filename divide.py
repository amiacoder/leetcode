class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend if dividend > 0 else min(-dividend, 2**31-1)
        if (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0):
            return self.getResult(abs(dividend), abs(divisor))
        else:
            return -self.getResult(abs(dividend), abs(divisor))

    def getResult(self, dividend, divisor):
        i = 0
        origin_divisor = divisor
        last_divisor = divisor
        while dividend - divisor >= 0:
            i = 2**i
            last_divisor = divisor
            divisor += divisor
        if i < 1:
            return i
        return i + self.getResult(dividend-last_divisor, origin_divisor)
