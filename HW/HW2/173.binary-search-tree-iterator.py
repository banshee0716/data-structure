#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        # 做一個容器，然後把所有東西塞進去
        self.stack = []
        self.pushAll(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        # 回傳是不是還有下一個node
        return self.stack

    # @return an integer, the next smallest number
    def next(self):
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.val

    def pushAll(self, node):
        # 把所有東西放進去
        while node is not None:
            self.stack.append(node)
            node = node.left


"""
實作一個可以把BST inorder traversal 的 iterator
"""
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
