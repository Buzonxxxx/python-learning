
def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        if (len(s) == 0): return False
        result = []
        for char in s:
            if (char == '('): result.append(')')
            elif (char == '['): result.append(']')
            elif (char == '{'): result.append('}')
            elif (len(result) == 0 or char != result.pop()): 
                return False
        if (len(result) == 0): return True
        return False

print(isValid('{[]}')); # True
print(isValid('((')); # False
print(isValid('()')); # True
print(isValid('[(])')); # False