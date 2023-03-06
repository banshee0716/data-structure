#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
"""
這段程式碼是要在給定的數組中找出中心索引（中心索引是指左邊元素之和等於右邊元素之和的索引），
如果不存在中心索引則返回-1。"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_nums, l = sum(nums), 0  # 計算整個數組的總和以及左邊元素之和的初始值

        for i, num in enumerate(nums):  # 枚舉每個元素
            if sum_nums - num == 2 * l:  # 如果右邊元素之和等於左邊元素之和
                return i  # 返回中心索引
            l += num  # 更新左邊元素之和

        return -1  # 如果沒有中心索引則返回-1


"""
時間複雜度：O(n)，其中n是數組的長度。因為需要遍歷整個數組，所以時間複雜度是O(n)。

空間複雜度：O(1)。除了一些變量外，沒有使用任何額外的空間，所以空間複雜度是O(1)。

"""

# @lc code=end
