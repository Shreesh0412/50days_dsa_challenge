class Solution(object):
    def peakIndexInMountainArray(self, arr):
        l=0
        r=len(arr)-1
        mid=0
        while l<r:
            mid=(l+r)//2
            if arr[mid]<arr[mid+1]:
                l=mid+1
            elif arr[mid]>arr[mid+1]:
                r=mid
        return l
