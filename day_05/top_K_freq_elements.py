class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        if len(nums)<=1:
            return nums
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        if len(d)==1:
            return d.keys()
        d=sorted(d.items(),key=lambda x: x[1],reverse=True)
        a=[]
        b=0
        for i in range(0,k):
            b=(d[i][0])
            a.append(b)
        return a
