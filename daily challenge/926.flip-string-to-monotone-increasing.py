#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#

# @lc code=start
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones, res = 0, 0
        for num in s:
            if num == "1":
                ones += 1
            elif ones:
                res += 1
                ones -= 1

        return res


# @lc code=end
