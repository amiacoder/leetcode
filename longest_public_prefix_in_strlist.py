class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or strs.count == 0:
            return ''
        if strs.count < 2:
            return strs[1]
        i = 0
        publis_str = ''
        while True:
            pre_str = None
            is_public_str = False
            for s in strs:
                if i >= len(s):
                    is_public_str = False
                else:
                    is_public_str =  (not pre_str or pre_str == s[i])
                    pre_str = s[i]
                if not is_public_str:
                    break
            if is_public_str:
                publis_str += pre_str
                i += 1
            else:
                break

        return publis_str
                
