class Solution(object):
    def repeatedCharacter(self, s):
        letter=set()
        for i in s:
            if i in letter:
                return i
            letter.add(i)
        