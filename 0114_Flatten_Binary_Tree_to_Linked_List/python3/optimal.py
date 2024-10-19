class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self._flatten(root)

    def _flatten(self, root: Optional[TreeNode]) -> TreeNode:
        if root is None:
            return None
        elif root.left is None and root.right is None:
            return root
        elif root.left is None:
            return self._flatten(root.right)
        elif root.right is None:
            root.right = root.left
            root.left = None
            return self._flatten(root.right)
        else:
            originalLeft = root.left
            originalRight = root.right
            lastLeft = self._flatten(originalLeft)
            if lastLeft is not None:
                lastLeft.right = originalRight
                root.right = originalLeft
                root.left = None
            lastRight = self._flatten(originalRight)
            return lastRight
