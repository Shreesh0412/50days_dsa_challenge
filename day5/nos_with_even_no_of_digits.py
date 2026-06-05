class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in nums:
            a=len(str(i))
            if a%2==0:
                c+=1
        return c
