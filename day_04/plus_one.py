class Solution(object):
    def plusOne(self, digits):
        digits[-1]+=1
        a=len(digits)
        for i in range(a-1,0,-1):
            if digits[i]==10:
                digits[i]=0
                digits[i-1]+=1
        if digits[0]==10:
            digits[0]=0
            digits.insert(0,1)
        return digits
