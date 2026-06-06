class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        a=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            b=i+1
            c=len(nums)-1
            while b<c:
                total=nums[i]+nums[b]+nums[c]
                if total<0:
                    b+=1
                elif total>0:
                    c-=1
                else:
                    a.append([nums[i],nums[b],nums[c]])
                    b+=1
                    c-=1
                    while b<c and nums[b]==nums[b-1]:
                        b+=1
                    while b<c and nums[c]==nums[c+1]:
                        c-=1
        return a
