# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        self.count=0
        prefix={0:1}
        def dfs(node,currsum):
            if not node:
                return
            currsum+=node.val
            self.count+=prefix.get(currsum-targetSum,0)
            prefix[currsum]=prefix.get(currsum,0)+1
            dfs(node.left,currsum)
            dfs(node.right,currsum)
            prefix[currsum]-=1
        dfs(root,0)
        return self.count
