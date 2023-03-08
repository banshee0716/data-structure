#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        sum_nums = 1
        for i in range(len(nums)):
            sum_nums *= nums[i]
        for i in range(len(nums)):
            ans.append(sum_nums // nums[i])
        return ans 
#這段程式碼沒有處理到nums[i] == 0的狀況會噴false
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = 1
        n = len(nums)
        ans = [1] * n
        for i in range(n):
            ans[i] *= prev
            prev *= nums[i]
        """
        此刻的陣列狀態(以範例測資為例[1, 2, 3, 4]):
        nums[i] = nums[i]*nums[i-1]...*nums[0]
        nums = [nums[0],nums[0]*nums[1], nums[0]*nums[1]*nums[2], nums[0]...*nums[3]]
        可以看出，其實還是欠缺了右半部分的乘積，所以我們還是得從右邊再乘回去一次。
        """
        prev = 1

        for i in range(n - 1, -1, -1):
            ans[i] *= prev
            prev *= nums[i]

        return ans
# O(2N)

# @lc code=end
