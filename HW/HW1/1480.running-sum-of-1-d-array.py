#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # 從第二個元素開始遍歷，將當前元素加上前一個元素的值，得到該元素的運行總和
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return nums


"""
時間複雜度分析：

遍歷給定的數組，時間複雜度為O(n)，其中n是給定數組的長度。
空間複雜度分析：

原地修改給定的數組，不需要額外的空間，空間複雜度為O(1)。
"""
# @lc code=end
