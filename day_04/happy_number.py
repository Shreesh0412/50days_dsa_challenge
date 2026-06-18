class Solution(object):
    def isHappy(self, n):
        a=set()
        while n!=1:
            if n in a:
                return False
            a.add(n)
            b=0
            while n>0:
                c=n%10
                b+=c*c
                n//=10
            n=b
        return True
