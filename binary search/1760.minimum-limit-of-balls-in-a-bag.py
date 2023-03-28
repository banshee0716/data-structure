#
# @lc app=leetcode id=1760 lang=python3
#
# [1760] Minimum Limit of Balls in a Bag
#

# @lc code=start
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # the maximum size increases the minimum number of bags decreases so we can binary search the maximum size
        def canDivide(size: int) -> bool:
          # return sum(balls // size - (1 if balls % size == 0 else 0) for balls in nums) <= maxOperations
            return sum((balls - 1) // size for balls in nums) <= maxOperations
        
        lo, hi = 1, 10 ** 9 + 1
        while lo < hi:
            size = lo + hi >> 1
            if canDivide(size):
                hi = size
            else:
                lo = size + 1
        return lo

# @lc code=end
