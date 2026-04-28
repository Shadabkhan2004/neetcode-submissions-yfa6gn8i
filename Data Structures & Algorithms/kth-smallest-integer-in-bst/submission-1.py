# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        curr = root
        def inorder(curr):
            if not curr:
                return
            inorder(curr.left)
            arr.append(curr.val)
            inorder(curr.right)
            
        inorder(curr)
        small = arr[k-1]

        return small
