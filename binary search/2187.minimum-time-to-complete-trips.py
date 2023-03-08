#
# @lc app=leetcode id=2187 lang=python3
#
# [2187] Minimum Time to Complete Trips
#

# @lc code=start
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def trip_counter(num):
            i = 0
            trips = 0
            while i < len(time):
                trips += num // time[i]
                i += 1
                if trips > totalTrips:
                    break
            return trips

        # 初始化二分搜尋範圍
        start = 1
        end = totalTrips * min(time)

        # 進行二分搜尋
        while start <= end:
            mid = (start + end) // 2  # 取中間值
            trips = trip_counter(mid)  # 計算在mid時間內可以完成的旅程數量

            # 根據trips的大小調整二分搜尋範圍
            if trips >= totalTrips:
                end = mid - 1
            else:
                start = mid + 1

        return start  # 因為start代表的時間一定可以完成totalTrips次旅程，所以start是最小可能的答案


"""
時間複雜度：O(N * log W)，其中N是time列表的長度，W是所有時間中的最大值。check_status函式中的for循環將遍歷整個time列表，而while循環最多只需要log W次迭代。

空間複雜度：O(1)，只使用了有限的變量空間，與輸入數據大小無關。
"""

# @lc code=end
