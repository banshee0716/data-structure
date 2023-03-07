#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 當head為空節點時，直接回傳head
        if not head:
            return head
        # odd表示奇數節點，even表示偶數節點
        odd, even = head, head.next
        # 記錄偶數節點的起始節點
        even_head = even
        # 交替將奇數節點與偶數節點相連
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        # 將奇數節點的尾節點指向偶數節點的起始節點
        odd.next = even_head
        return head


"""
時間複雜度：O(n)，其中n為鏈表節點的個數。這是因為程式只需遍歷整個鏈表一次，每個節點只被訪問一次。
空間複雜度：O(1)，空間使用量固定。
"""
# @lc code=end
