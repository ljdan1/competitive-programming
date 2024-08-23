class Solution(object):
    def productExceptSelf(self, nums):
        output=[1]*len(nums)
        i=1
        while i<len(nums):
            output[i]=nums[i-1]*output[i-1]
            i+=1
        mul=1
        i=len(nums)-2
        while i>=0:
            mul*=nums[i+1]
            output[i]*=mul
            i-=1
        return output
