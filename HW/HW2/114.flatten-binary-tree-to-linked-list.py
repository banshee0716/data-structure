#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None  # 記錄前一個節點

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:  # 當節點為空時，返回空
            return None

        # 用遞歸的方式對右子樹進行展開
        self.flatten(root.right)
        # 再對左子樹進行展開
        self.flatten(root.left)

        # 將前一個節點作為當前節點的右子節點
        root.right = self.prev
        root.left = None  # 將左子節點設為空
        self.prev = root  # 記錄當前節點


# @lc code=end
