class Solution(object):
    def moveZeroes(self, nums):
        n=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[n]=nums[i]
                n+=1
        for i in range(n, len(nums)):
            nums[i] = 0
        return nums
         
        
 
        