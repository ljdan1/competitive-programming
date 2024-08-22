class Solution(object):
    def backspaceCompare(self, s, t):
        s_sets=[]
        t_sets=[]
        for i in s:
            if i=="#":
                if s_sets:
                    s_sets.pop()
            else:
                s_sets.append(i)
        for i in t:
            if i=="#":
                if t_sets:
                    t_sets.pop()
            else:
                t_sets.append(i)
        if s_sets==t_sets:
            return True
        else:
            return False
        