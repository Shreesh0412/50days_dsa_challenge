class Solution(object):
    def twoSum(self, nums, target):
        a=len(nums)
        b={}
        c=0
        for i in range(0,a):
            c=target-nums[i]
            if c in b:
                return [b[c],i]
            b[nums[i]]=i
