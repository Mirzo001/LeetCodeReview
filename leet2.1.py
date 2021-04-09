class Solution:
    def reverse(self, x: int) -> int:
        intMax = 2**31-1
        intMin = -2**31
        rev = 0
        sign = 1
        if x > intMax or x < intMin:
            return 0
        if x < 0:
            sign = -1 
            x *= sign 
            # -123
        while x != 0:
            pop = x % 10
            # pop = -123 % 10 = 7
            x = int(x/10) 
            # -123 = -123/10 = -12.3
            rev = rev * 10 + pop
            # 0 = 0 * 10 + 7 = 7
        return 0 if rev>intMax or rev<intMin else rev*sign
x = 123
y = Solution.reverse(x, 123)
print(y)