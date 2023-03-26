#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.sqrt(c))
        while left <= right:
            if left * left + right * right == c:
                return True
            elif left * left + right * right > c:
                right -= 1
            else:
                left += 1
        return False


# @lc code=end
