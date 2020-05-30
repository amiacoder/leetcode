class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        test = '#'+'#'.join(s)+'#'
        max_len = 0
        for i in range(len(test)):
            left = i - 1
            right = i + 1
            step = 0
            while left >= 0 and right < len(test) and test[left] == test[right]:
                left -= 1
                right += 1
                step += 1
            if step > max_len:
                max_len = step
                start = (i - max_len) // 2
        return s[start: start + max_len]
