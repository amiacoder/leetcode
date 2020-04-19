class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = True if x < 0 else False
        s = str(x)[::-1]
        if flag:
            s = str(x)[1:][::-1]
        if len(bin(int(s))) > 33:
            return 0
        return (-int(s) if flag else int(s))
