class Solution(object):
    def findLHS(self, nums):
        long=0
        count=collections.Counter(nums)
        for i in count.keys():
            if i+1 in count:
                long= max(long,count[i]+count[i+1])
        return long