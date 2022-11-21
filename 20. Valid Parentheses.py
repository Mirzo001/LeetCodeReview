

# "()"
# "()[]{}"
# "(]"
s = "()[]}"

def isValid(s):
    paranthesis = { '(':')', '{':'}', '[':']' }
    stack = []
    for i in s:
        if i in paranthesis:
            stack.append(i)
        elif len(stack) == 0 or paranthesis[stack.pop()] != i:
            return False
    
    return len(stack) == 0

x=isValid(s)        
print(x)