class Solution(object):
    def productExceptSelf(self, nums):
        a=len(nums)
        b=[1]*a
        c,d=1,1
        for i in range(a):
            b[i]=c
            c=c*nums[i]
        for i in range(a-1,-1,-1):
            b[i]=b[i]*d
            d=d*nums[i]
        return b
