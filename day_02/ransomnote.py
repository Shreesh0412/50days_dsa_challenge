class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        a={}
        b={}
        for i in ransomNote:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in magazine:
            if i in b:
                b[i]+=1
            else:
                b[i]=1
        for i in a:
            if i not in b or b[i]<a[i]:
                return False
        return True
