class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''
        i = 0
        while num > 0:
            n = num % 10
            if i == 0:
                collection = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
                result = collection[n] + result
            elif i == 1:
                collection = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
                result = collection[n] + result
            elif i == 2:
                collection = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
                result = collection[n] + result
            elif i == 3:
                collection = ['', 'M', 'MM', 'MMM']
                result = collection[n] + result
            num = num / 10
            i += 1
        return result


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''
        roman_collection = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I' ]
        number_collection = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        while i < 13:
            while num - number_collection[i] >= 0:
                result += roman_collection[i]
                num -= number_collection[i]
            i += 1
        return result


