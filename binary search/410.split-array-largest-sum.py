#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(threshold) -> bool:
            # TODO 等等實作他的判斷條件,找他的切割點切割成ｋ個
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > threshold:
                    total = num
                    count += 1
                    if count > k:
                        return False
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left


"""
二分搜尋找分割的臨界點，與１０１１題很像
"""
# @lc code=end
