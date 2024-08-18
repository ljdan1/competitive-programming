class Solution(object):
    def removeDuplicates(self, s):
        letter=[]
        for i in s:
            if letter and letter[-1]==i:
                letter.pop()
            else:
                letter.append(i)
        return "".join(letter)