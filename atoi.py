c1ass Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str or len(str) == 0:
            return 0
        valid_char = None
        for char in str:
            if not valid_char:
                if char == ' ':
                    continue
                elif char == '-' or char == '+'  or char.isdigit():
                    valid_char = char
                else:
                    return 0
            else:
                if char.isdigit():
                    valid_char += char
                else:
                    break
        #print valid_char
        if not valid_char:
            return 0
        if valid_char[0] == '-':
            if len(valid_char) == 1:
                return 0;
            return -min(int(valid_char[1:]), 2**31)
        elif valid_char[0] == '+':
            valid_char = valid_char[1:]
        if len(valid_char) == 0:
            return 0;
        return min(int(valid_char), 2**31-1)
        

