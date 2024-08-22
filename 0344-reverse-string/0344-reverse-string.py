class Solution(object):
    def reverseString(self, s):
        stack=[]
        for i in s:
            stack.append(i)
        for i in range(len(stack)):
            s[i]=stack.pop()
        return stack
        