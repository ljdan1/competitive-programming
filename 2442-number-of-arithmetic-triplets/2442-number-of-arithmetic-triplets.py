class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        count1=collections.Counter()
        count2=collections.Counter()
        total=0
        for i in nums:
            total+=count2[i-diff]
            count2[i]+=count1[i-diff]
            count1[i]+=1
        return total

        