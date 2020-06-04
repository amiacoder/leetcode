class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        v_map = {'(': ')', '{': '}', '[': ']'}
        list_to_remove = []
        start = 0
        is_valid_str = True
        while start < len(s):
            if s[start] not in v_map:
                if s[start] not in list_to_remove:
                    is_valid_str = False
                    break
                else:
                    if list_to_remove[len(list_to_remove)-1] == s[start]:
                        del(list_to_remove[len(list_to_remove)-1])
                    else:
                        is_valid_str = False
                        break
            else:
                list_to_remove.append(v_map[s[start]])
            start += 1
        return (is_valid_str and len(list_to_remove) == 0)
