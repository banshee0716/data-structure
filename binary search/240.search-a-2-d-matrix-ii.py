#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
            return False
        h, w = len(matrix), len(matrix[0])

        for row in matrix:

            # range check
            if row[0] <= target <= row[-1]:
                left, right = 0, w - 1

                while left <= right:
                    mid = left + (right - left) // 2
                    mid_value = row[mid]
                    if target > mid_value:
                        left = mid + 1
                    elif target < mid_value:
                        right = mid - 1
                    else:
                        return True
        return False


# @lc code=end
