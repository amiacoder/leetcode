
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        value_map = {'2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z'],
                    }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [_ for _ in value_map[digits]]
        start_chars = value_map[digits[0]]
        sub_result = self.letterCombinations(digits[1:])
        result = []
        for char in start_chars:
            [result.append(char+_) for _ in sub_result]
        return result
