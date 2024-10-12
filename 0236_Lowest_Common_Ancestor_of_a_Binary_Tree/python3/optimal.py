# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node, isLCA = self._lowestCommonAncestor(root, p, q)
        return node

    def _lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> ('TreeNode', bool):
        if root is None:
            return (None, False)
        left, leftIsLCA = self._lowestCommonAncestor(root.left, p, q)
        right, rightIsLCA = self._lowestCommonAncestor(root.right, p, q)
        haveLeft = left is not None
        haveRight = right is not None
        isTarget = root.val == p.val or root.val == q.val

        if haveLeft and leftIsLCA:                   return (left, leftIsLCA)   # Left is already our LCA so just pass that up
        elif haveRight and rightIsLCA:               return (right, rightIsLCA) # Right is already our LCA so just pass that up
        elif haveLeft and haveRight:                 return (root, True)        # This node is our LCA, we need to stop here altogether
        elif (haveLeft or haveRight) and (isTarget): return (root, True)        # This node is our LCA, we need to stop here altogether
        elif haveLeft:                               return (left, False)
        elif haveRight:                              return (right, False)
        elif isTarget:                               return (root, False)       # This node is one of our nodes
        else:                                        return (None, False)       # Path exhausted
