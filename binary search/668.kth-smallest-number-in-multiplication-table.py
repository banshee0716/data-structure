#
# @lc app=leetcode id=668 lang=python3
#
# [668] Kth Smallest Number in Multiplication Table
#

# @lc code=start
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(num) -> bool:
            count = 0
            for val in range(1, m + 1):
                add = min(num // val, n)  # 計算每一行中小於 num 的數量
                if add == 0:  # 如果小於 num 的數量為 0，則提前退出
                    break
                count += add  # 累計小於 num 的數量
            return count >= k  # 判斷小於 num 的數量是否大於等於 k

        left, right = 1, n * m
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):  # 如果小於等於 mid 的數量大於等於 k，將範圍縮小到左半部分
                right = mid
            else:  # 如果小於等於 mid 的數量小於 k，將範圍縮小到右半部分
                left = mid + 1
        return left  # 返回最終結果


"""
這個問題是要求在由1到m、1到n的矩陣中，第k小的數字是什麼。可以使用二分查找來解決。

首先，觀察到這個矩陣中每個數字都是由1到m的數字中的一個乘以1到n的數字中的一個組成。因此，我們可以將矩陣中的每個數字都表示為num = i * j，其中i是1到m的數字，j是1到n的數字。
接下來，我們可以對num進行二分查找，直到找到第k小的數字為止。具體來說，我們可以通過對num進行二分查找來計算小於等於num的數字有多少個。
為了計算這個數量，我們可以逐行遍歷矩陣，計算每一行中小於等於mid的數字有多少個。如果總數小於k，那麼第k小的數字一定大於mid，因此我們可以將left設為mid + 1；
否則，第k小的數字一定小於等於mid，因此我們可以將right設為mid。

時間複雜度：
二分查找的時間複雜度為O(log(mn))，每次二分查找需要遍歷整個矩陣計算數量，因此總時間複雜度為O(m log(mn))。

空間複雜度：
需要常數額外空間存儲變量，因此空間複雜度為O(1)。

"""
# @lc code=end
