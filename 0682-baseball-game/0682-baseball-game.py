class Solution(object):
    def calPoints(self, operations):
        score=[]
        for i in operations:
            if i=='+':
                score.append(score[-1]+score[-2]) 
            elif i=='D':
                score.append(2*score[-1])
            elif i=='C':
                score.pop()
            else:
                score.append(int(i)) 

        return sum(score) 
