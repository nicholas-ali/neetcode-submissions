# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = -1
        max_lefts = float('-inf')
        val = -1

        q = [(root, 0, 0)]

        while q:
            node, depth, lefts = q.pop()
            if depth == max_depth and lefts > max_lefts:
                max_lefts = lefts
                val = node.val
            elif depth > max_depth:
                max_depth = depth
                max_lefts = lefts
                val = node.val
            if node.right:
                q.append((node.right, depth+1, lefts-1))
            if node.left:
                q.append((node.left, depth+1, lefts+1))

        return val