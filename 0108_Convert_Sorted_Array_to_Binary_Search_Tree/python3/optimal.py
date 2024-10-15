class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        mid = n // 2
        subarrayLeft = nums[0:mid]
        subarrayRight = nums[mid+1:n]
        noLeft = len(subarrayLeft) == 0
        noRight = len(subarrayRight) == 0

        if noLeft and noRight:
            return TreeNode(nums[mid], None, None)
        elif noLeft:
            nodeRight = self.sortedArrayToBST(subarrayRight)
            return TreeNode(nums[mid], None, nodeRight)
        elif noRight:
            nodeLeft = self.sortedArrayToBST(subarrayLeft)
            return TreeNode(nums[mid], nodeLeft, None)
        else:
            nodeLeft = self.sortedArrayToBST(subarrayLeft)
            nodeRight = self.sortedArrayToBST(subarrayRight)
            return TreeNode(nums[mid], nodeLeft, nodeRight)
