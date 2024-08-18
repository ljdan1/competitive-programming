class Solution(object):
    def numIdenticalPairs(self, nums):
        count = {}  
        good_pairs = 0
        for i in nums:
            if i in count:
                good_pairs += count[i]
                count[i] += 1
            else:
                count[i] = 1
        return good_pairs
        