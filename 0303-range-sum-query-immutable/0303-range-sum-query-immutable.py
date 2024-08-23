class NumArray(object):

    def __init__(self, nums):
        
        self.nums=nums
        n=0
        for i in range(len(nums)):
            self.nums[i]+=n
            n=self.nums[i]
        

    def sumRange(self, left, right):
       
        if left==0:
           return self.nums[right]
        else:
           return self.nums[right]-self.nums[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)