#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#

# @lc code=start
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def enough(distance) -> bool:  # two pointers
            count, i, j = 0, 0, 0
            while i < n or j < n:

                while j < n and nums[j] - nums[i] <= distance:  # move fast pointer
                    j += 1

                count += j - i - 1  # count pairs

                i += 1  # move slow pointer
            return count >= k

        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left


"""
一對整數 a 和 b 的距離定義為 a 和 b 之間的絕對差。
給定一個整數數組 nums 和一個整數 k，返回所有對 nums[i] 和 nums[j] 中第 k 個最小距離，其中 0 <= i < j < nums.length。
"""

"""
與上面的 LC 668 非常相似，都是關於尋找 Kth-Smallest 的。就像LC 668一樣，我們可以設計一個足夠的函數，給定一個輸入距離，判斷是否至少有k對距離小於或等於distance。
我們可以對輸入數組進行排序，並使用兩個指針（快指針和慢指針，指向一對）來掃描它。兩個指針都從最左端開始。
如果指向的當前對的距離小於或等於 distance，則這些指針之間的所有對都是有效的（因為數組已經排序），我們向前移動快速指針。
否則，我們向前移動慢指針。當兩個指針都到達最右端時，我們完成掃描並查看總數是否超過 k。
"""
# @lc code=end
