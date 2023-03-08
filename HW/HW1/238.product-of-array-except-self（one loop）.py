#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
"""class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        sum_nums = 1
        for i in range(len(nums)):
            sum_nums *= nums[i]#會溢位"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        left = 1
        right = 1

        for i in range(len(nums)):
            ans[i] *= left
            ans[-1 - i] *= right
            left *= nums[i]
            right *= nums[-1 - i]

        return ans
    # O(N)


# @lc code=end
