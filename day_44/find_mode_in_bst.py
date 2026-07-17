# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findMode(self, root):
        freq = {}

        def dfs(node):
            if not node:
                return

            freq[node.val] = freq.get(node.val, 0) + 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        maxFreq = max(freq.values())

        ans = []
        for key in freq:
            if freq[key] == maxFreq:
                ans.append(key)

        return ans
