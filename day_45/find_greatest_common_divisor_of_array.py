class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small=min(nums)
        large=max(nums)
        while large%small!=0:
            large,small=small,large%small
        return small
