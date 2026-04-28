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
        def preorder(curr):
            if not curr:
                return
            preorder(curr.left)
            arr.append(curr.val)
            preorder(curr.right)
            
        preorder(curr)
        small = arr[k-1]

        return small
