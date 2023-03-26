#
# @lc app=leetcode id=1855 lang=python3
#
# [1855] Maximum Distance Between a Pair of Values
#

# @lc code=start
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j, n, m, res = 0, 0, len(nums1), len(nums2), 0
        while i < n and j < m:
            if nums1[i] > nums2[j]:
                i += 1
            else:
                res = max(res, j - i)
                j += 1
        return res


# @lc code=end
