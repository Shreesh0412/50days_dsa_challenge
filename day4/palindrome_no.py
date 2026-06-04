class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        c=x
        a=0
        b=0
        while x>0:
            a=x%10
            b=(b*10)+a
            x=x//10
        if c==b:
            return True
        else:
            return False
