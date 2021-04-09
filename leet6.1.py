def isValid(self, s: str) -> bool:
        
        opening_brackets = []
        
        open_to_close = {
            "(": ")", 
            "[": "]",
            "{": "}"
        }
        
        for char in s:
            
            # Is char an opening bracket?
            if char in open_to_close:
                opening_brackets.append(char)

            # Is stack empty?
            elif not opening_brackets:
                return False
                
            # Does char "complete" the last opening braket?  
            else:
                opening = opening_brackets.pop()
                closing = open_to_close[opening]
                if char != closing:
                    return False
                
        # Return True if stack is empty, else False 
        return not opening_brackets
s = "{{{{{{{}}}}}}}"
x = isValid('', s)
print(x)