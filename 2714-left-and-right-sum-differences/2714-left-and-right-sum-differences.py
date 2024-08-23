class Solution(object):
    def leftRightDifference(self, nums):
        leftsum=0
        rightsum=sum(nums)
        answer=[0]*len(nums)
        for i in range(len(nums)):
            rightsum -= nums[i]
            answer[i]=abs(leftsum-rightsum)
            leftsum += nums[i]
        return answer
        
        
       
            
