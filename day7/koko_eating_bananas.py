class Solution(object):
    def minEatingSpeed(self, piles, h):
        l=1
        r=max(piles)
        a=r
        while l<=r:
            k=(l+r)//2
            b=0
            for i in piles:
                b+=(i+k-1)//k
            if b<=h:
                a=k
                r=k-1
            else:
                l=k+1
        return a
