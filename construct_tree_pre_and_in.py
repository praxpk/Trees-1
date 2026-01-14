# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(preorder, inorder)

    def helper(self, preorder, inorder):
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root = preorder[0]

        inorderRootPos = inorder.index(root)

        inLeft = inorder[:inorderRootPos]
        preLeft = preorder[1 : 1 + len(inLeft)]
        inRight = inorder[inorderRootPos + 1 :]
        preRight = preorder[1 + len(preLeft) :]
        t1 = TreeNode(root)
        t1.left = self.helper(preLeft, inLeft)
        t1.right = self.helper(preRight, inRight)
        return t1
