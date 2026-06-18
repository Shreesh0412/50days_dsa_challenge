class Solution(object):
    def mySqrt(self, x):
        if x==0:
            return 0
        l=1
        r=x
        a=1
        while l<=r:
            mid=(l+r)//2
            if mid**2>x:
                r=mid-1
            else:
                a=mid
                l=mid+1
        return a
