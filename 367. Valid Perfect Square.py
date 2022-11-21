def isPerfectSquare(num: int):
    r = num
    while r*r > num:
        r = (r + num/r) // 2
    return r*r == num
           
print(isPerfectSquare(15))
