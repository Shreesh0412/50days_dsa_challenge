class Solution(object):
    def searchRange(self, nums, target):
        def lowerbound():
            a=len(nums)
            lb=a
            r=a-1
            l=0
            while l<=r:
                mid=(l+r)//2
                if nums[mid]>=target:
                    lb=mid
                    r=mid-1
                else:
                    l=mid+1
            return lb
        def upperbound():
            a=len(nums)
            ub=a
            r=a-1
            l=0
            while l<=r:
                mid=(l+r)//2
                if nums[mid]>target:
                    ub=mid
                    r=mid-1
                else:
                    l=mid+1
            return ub
        lb=lowerbound()
        ub=upperbound()
        if lb==ub:
            return[-1,-1]        
        else:
            return[lb,ub-1]
