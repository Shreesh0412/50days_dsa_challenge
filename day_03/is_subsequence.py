class Solution(object):
    def isSubsequence(self, s, t):
        a=0
        for i in range(0,len(t)):
            if a<len(s) and s[a]==t[i]:
                a+=1
        if len(s)==a:
            return True
        else:
            return False
