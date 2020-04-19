class Solution:
    def isPalindrome(self, x):
        # if x == 0:
        #     return True
        # elif x < 0:
        #     return False
        # else:
        #     return str(x)[::-1] == str(x)

        if x < 0:
            return False
        elif x == 0:
            return True
        elif x%10 == 0:
            return False
        else:
            revert_num = 0
            while x > revert_num:
                revert_num = revert_num * 10 + x%10
                x //= 10
            return x == revert_num or x == revert_num // 10
