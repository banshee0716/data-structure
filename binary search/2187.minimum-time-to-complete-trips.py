#
# @lc app=leetcode id=2187 lang=python3
#
# [2187] Minimum Time to Complete Trips
#

# @lc code=start
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        right = min(time) * totalTrips + 1 
        # 記數二分搜尋問題的解答，最右邊子區間為最差情況下的答案，即所有司機都需要前往一個站點且所需時間為time中最小值的總和。
        left = 0
        answer = 0

        def check(expected_time: int) -> int:
            nonlocal answer　#把ans設為全域變數
            count = 0
            for i in time:
                count += expected_time // i # 期望時間expected_time內可完成的總行程次數應為expected_time // i的整數部分
            if count < totalTrips:
                return 1 # 因為行程數量不足，left需要移動到mid
            elif count >= totalTrips:
                answer = expected_time # 儲存最新的答案。這是保證為最小可能答案。
                return -1 # 因為行程數量大於或等於要求，right需要移動到mid

        while left < right-1: # 在二分搜尋仍可繼續的情況下
            mid = left + (right-left) // 2 # mid是當前的期望時間
            status = check(mid) # check函式中的返回值1/-1決定了要移動哪個指針。
            if status == 1:
                left = mid
            else:
                right = mid
                
        return answer
'''
時間複雜度：O(N * log W)，其中N是time列表的長度，W是所有時間中的最大值。check_status函式中的for循環將遍歷整個time列表，而while循環最多只需要log W次迭代。

空間複雜度：O(1)，只使用了有限的變量空間，與輸入數據大小無關。
'''

# @lc code=end

