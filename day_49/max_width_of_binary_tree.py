# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        from collections import deque
        if not root:
            return 0
        queue=deque([(root,0)])
        max_width=0
        while queue:
            level_size=len(queue)
            i,first=queue[0]
            last=first
            for i in range(level_size):
                node,index=queue.popleft()
                index-=first
                last=index
                if node.left:
                    queue.append((node.left,2*index+1))
                if node.right:
                    queue.append((node.right,2*index+2))
            max_width=max(max_width,last+1)
        return max_width
