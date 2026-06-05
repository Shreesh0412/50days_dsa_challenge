class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        a,b=0,0
        for i in columnTitle:
            a=ord(i)-ord("A")+1
            b=b*26+a
        return b
