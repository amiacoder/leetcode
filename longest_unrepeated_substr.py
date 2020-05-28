class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        start = 0
        cur_len = 0
        max_length = 0
        look_up = set()
        for i in range(0, len(s)):
            cur_len += 1
            if s[i] in look_up:
                while s[i] in look_up:
                    look_up.remove(s[start])
                    start += 1
                    cur_len -= 1
            look_up.add(s[i])
            if cur_len > max_length: max_length = cur_len
        return max_length
