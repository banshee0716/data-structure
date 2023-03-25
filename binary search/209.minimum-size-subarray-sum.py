#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low, high = 1, len(nums) + 1  # 初始化二分搜索的邊界

        # 進行二分搜索
        while low < high:
            mid = (low + high) // 2  # 計算中間值

            # 利用滑動窗口檢查是否存在大小為 mid 的子數組，其和大於等於 target
            if self.slidingWin(target, nums, mid):
                high = mid  # 縮小右邊界
            else:
                low = mid + 1  # 縮小左邊界

        # 檢查最小窗口大小是否滿足條件，如果滿足則返回窗口大小，否則返回 0
        if self.slidingWin(target, nums, low):
            return low
        else:
            return 0

    def slidingWin(self, target, nums, k):
        curSum = 0  # 初始化當前子數組的和
        maxSum = 0  # 初始化最大子數組的和
        l = 0  # 初始化滑動窗口的左邊界

        # 遍歷數組
        for i in range(len(nums)):
            curSum += nums[i]  # 更新當前子數組的和

            # 如果子數組的大小超過 k，則更新左邊界並減去左邊界對應的數值
            if i > k - 1:
                curSum -= nums[l]
                l += 1

            # 更新最大子數組的和
            maxSum = max(curSum, maxSum)

        # 檢查最大子數組的和是否大於等於目標值
        return maxSum >= target


"""
時間複雜度：O(n * log n)，其中 n 是 nums 的長度。這是因為對於每個二分搜索的迭代（共 log n 次），需要遍歷整個數組以使用滑動窗口檢查條件（O(n)）。

空間複雜度：O(1)。算法使用了常數級別的額外空間，因此空間複雜度為 O(1)。
"""

# @lc code=end
