class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        if len(s) < 3:
            return s
        l = [[s[0]]]
        last_position = [0, 0, 0] # 第几个字数组，第几个位置，是否z 平字边
        i = 1
        while i < len(s):
            if last_position[2] == 0:
                # z 横字边
                if last_position[1] == numRows - 1:
                    # 上次已经填满z 横字边
                    last_position[0] = last_position[0] + 1
                    last_position[1] = numRows - 2
                    last_position[2] = 1
                    sub_l = []
                    l.append(sub_l)
                    for j in range(0, numRows):
                        if j == numRows - 2:
                            sub_l.append(s[i])
                        else:
                            sub_l.append(-1)
                else:
                    sub_l = l[last_position[0]]
                    sub_l.append(s[i])
                    last_position[1] = last_position[1] + 1
            else:
                # 上次不是z 横字边
                if last_position[1] == 0:
                    #刚好填到下一个 z 字横边
                    l[last_position[0]] = l[last_position[0]][0:1]
                    sub_l = l[last_position[0]]
                    last_position[1] = last_position[1] + 1
                    last_position[2] = 0
                    sub_l.append(s[i])
                else:
                    last_position[0] = last_position[0] + 1
                    last_position[1] =  last_position[1] - 1
                    last_position[2] = 1
                    sub_l = []
                    l.append(sub_l)
                    for j in range(0, numRows):
                        if j == last_position[1]:
                            sub_l.append(s[i])
                        else:
                            sub_l.append(-1)
            i = i + 1
        final_s = ''
        for j in range(0, numRows):
            for i in range(0, len(l)):
                if j < len(l[i]) and not isinstance(l[i][j], int):
                    final_s = final_s + l[i][j]
        return final_s
