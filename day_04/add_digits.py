class Solution(object):
    def addDigits(self, num):
        def aa(n):
            a=str(n)
            b=0
            for i in a:
                b=b+int(i)
            if len(str(b))==1:
                return b
            else:
                return aa(b)
        return aa(num)
