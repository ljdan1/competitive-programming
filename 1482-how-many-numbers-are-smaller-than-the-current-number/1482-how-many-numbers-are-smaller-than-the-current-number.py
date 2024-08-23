class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        array=[]
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count+=1
            array.append(count)
            count=0
        return array