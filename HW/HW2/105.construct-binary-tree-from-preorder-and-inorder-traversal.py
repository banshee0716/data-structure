#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # 如果中序遍歷為空，則返回None
        if not inorder:
            return None

        # 建立根節點，其值為前序遍歷的第一個元素
        root = TreeNode(preorder.pop(0))

        # 找到根節點在中序遍歷中的位置
        index = inorder.index(root.val)
        # 如果要用比較底層的語言來刻，我會用二分搜尋來找INDEX但先不做討論。(O(logn))

        # 遞迴建立左子樹和右子樹
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index + 1 :])

        return root


"""
process()
preorder(root.left)
preorder(root.right)
"""

"""
inorder(root.left)
process()
inorder(root.right)
"""


# @lc code=end
