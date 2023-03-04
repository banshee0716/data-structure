#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 如果列表為空，則返回0
        if not nums:
            return 0
        # 如果列表只有一個元素，則檢查該元素是否等於k，是則返回1，否則返回0
        if len(nums) == 1:
            if nums[0] == k:
                return 1
            return 0

        ans, prefix_sum = 0, 0
        # 前綴和與出現次數的字典
        d = {0: 1}

        # 遍歷nums列表
        for num in nums:
            # 計算前綴和
            prefix_sum = prefix_sum + num
            # 如果存在一個前綴和等於prefix_sum - k，則將答案增加相應的出現次數
            if prefix_sum - k in d:
                ans = ans + d[prefix_sum - k]
            # 在字典中添加出現次數
            if prefix_sum not in d:
                d[prefix_sum] = 1
            else:
                d[prefix_sum] = d[prefix_sum] + 1

        # 返回答案
        return ans


"""
時間複雜度：O(n)，其中n是nums列表的長度。因為需要遍歷nums一次，並將它添加到哈希表中，這需要O(n)的時間。在哈希表中搜索特定的鍵需要O(1)的時間。
空間複雜度：O(n)，其中n是nums列表的長度。哈希表最多包含n個鍵值對，需要O(n)的空間。
"""

# @lc code=end
