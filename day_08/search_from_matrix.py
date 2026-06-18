class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        a=len(matrix)
        b=len(matrix[0])
        l=0
        r=a*b-1
        while l<=r:
            mid=(l+r)//2
            row=mid//b
            col=mid%b
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                r=mid-1
            else:
                l=mid+1
        return False
