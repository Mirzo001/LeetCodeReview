def isPalindrome(self, x: int) -> bool:
        if x > 0:
            temp = x
            rev_int_elements = []
            while temp > 0:
                digit = temp % 10
                rev_int_elements.append(digit)
                temp = temp // 10
            org_int_elements = rev_int_elements[::-1]
            return rev_int_elements == org_int_elements
        elif x == 0:
            return True
        else:
            return False
x = 34433443
y = isPalindrome(x, 1221)
print(y)