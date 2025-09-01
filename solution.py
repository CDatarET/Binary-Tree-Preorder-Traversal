# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorder(self, root, arr):
        if(root == None):
            return
        arr.append(root.val)
        self.preorder(root.left, arr)
        self.preorder(root.right, arr)

    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        arr = []
        self.preorder(root, arr)
        return(arr)
