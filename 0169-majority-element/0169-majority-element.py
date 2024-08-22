class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sets={}
        for i in nums:
            if i not in sets:
                sets[i]=1
            else:
                sets[i]+=1
            if sets[i]>len(nums)/2:
                return i
        