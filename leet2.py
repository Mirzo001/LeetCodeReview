def reverse(x: int) -> int:
        s = str(x)    
        reversed = int(s[::-1])
        if reversed > 2147483647:
            return 0
        return reversed if x > 0 else (reversed * -1)
x = reverse(x=1234567)
print(x)