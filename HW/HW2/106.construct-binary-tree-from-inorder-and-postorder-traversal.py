#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 定義一個遞迴函數helper，用於建立子樹
        def helper(post_beg, post_end, in_beg, in_end):
            # 如果後序遍歷序列的範圍為空，則返回None
            if post_end - post_beg <= 0:
                return None
            # 獲取當前子樹的根節點在中序遍歷序列中的索引
            ind = dic[postorder[post_end - 1]]
            # 創建根節點
            root = TreeNode(inorder[ind])
            # 遞迴建立左子樹和右子樹
            root.left = helper(post_beg, post_beg + ind - in_beg, in_beg, ind)
            root.right = helper(post_end - in_end + ind, post_end - 1, ind + 1, in_end)
            # 返回樹的根節點
            return root

        # 創建一個字典，用於快速查找中序遍歷序列中節點值對應的索引
        dic = {elem: it for it, elem in enumerate(inorder)}
        # 調用helper函數，傳入後序遍歷序列的範圍和中序遍歷序列的範圍
        # 範圍由起始位置和結束位置兩個變量構成
        return helper(0, len(postorder), 0, len(inorder))


# @lc code=end
