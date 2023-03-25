#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#

# @lc code=start
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # 定義一個輔助函數來檢查在給定的天數內是否可以製作指定數量的花束
        def feasible(days) -> bool:
            # 初始化花束數量和已檢查的花朵數量
            bonquets, flowers = 0, 0
            # 遍歷每一朵花的開花時間
            for bloom in bloomDay:
                if bloom > days:  # 如果開花時間大於給定的天數
                    flowers = 0  # 重新開始計算花朵數量
                else:
                    # 計算在這段時間內可以製作的花束數量和剩餘的花朵數量
                    bonquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            # 檢查是否可以製作至少m個花束
            return bonquets >= m

        # 如果總花朵數量小於需要的花朵數量，則返回-1
        if len(bloomDay) < m * k:
            return -1

        # 初始化二分搜索的邊界
        left, right = 1, max(bloomDay)

        # 進行二分搜索
        while left < right:
            mid = left + (right - left) // 2  # 計算中間值
            if feasible(mid):  # 如果可以製作指定數量的花束
                right = mid  # 縮小右邊界
            else:
                left = mid + 1  # 縮小左邊界

        # 返回最小的天數
        return left

"""
給定一個整數數組 bloomDay、一個整數 m 和一個整數 k。我們需要製作 m 束花束。
要製作花束，您需要使用花園中相鄰的 k 朵花。
花園由 n 朵花組成，第 i 朵花將在 bloomDay[i] 開花，然後可以用在一束花中。
返回您需要等待的最少天數才能從花園裡製作出 m 束花束。如果不可能使m個花束返回-1。
"""
# @lc code=end
