#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start

# 返回能在n天內運完的最小容量，如果能運送超過的量，就必定能運送更小的量
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity) -> bool:  # 返回是否可以在 D 天內運送所有包裹。
            day, total = 1, 0
            for weight in weights:
                total += weight
                if total > capacity:  # 太重等明天
                    total = weight
                    day += 1
                    if day > days:
                        return False
            return True

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):  # 先從正面邏輯開始，如果目前可行的話，往回找找看其他的容量能運送完全部。
                right = mid
            else:
                left = mid + 1
        return left


# @lc code=end
