#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def binarySearch(row):
            left, right = 0, len(row)
            while left < right:
                mid = left + (right - left) // 2
                if row[mid] < 0:
                    right = mid
                else:
                    left = mid + 1
            return len(row) - left

        count = 0
        for i in grid:
            count += binarySearch(i)
        return count


# @lc code=end
