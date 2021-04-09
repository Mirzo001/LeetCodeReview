class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        out = 0
        pre= dic[s[0]]
        # XVII
        for i,x in enumerate(s):
            if dic[x] > pre:
                out += dic[x]
                out -= 2*pre
                pre = dic[x]
            else:
                out += dic[x]
                pre = dic[x]
        return out
# s = 0
# y = Solution.romanToInt(s, "XVII")
# print(y)
s = 'XVII'
# 0 1 2 3
# X V I I
dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
pre= dic[s[0]]
print(pre)