class Solution(object):
    def isValid(self, s):
        stack=[]
        subset = {')':'(' ,'}':'{', ']':'['}  
        for i in s:
            if i in subset:
                if stack and stack[-1]==subset[i]:
                    stack.pop()
                else:
                    return False
            else:
                 stack.append(i)
        return  True if not stack else False