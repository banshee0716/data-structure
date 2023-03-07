#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_s, hash_t = {}, {}
        for i in range(len(s)):
            # 設置兩個hash map，檢測這兩個字串裡面的元素是否相互對應並計數
            if (
                s[i] in hash_s
                and hash_s[s[i]] != t[i]
                or t[i] in hash_t
                and hash_t[t[i]] != s[i]
            ):
                return False
            hash_s[s[i]] = t[i]
            hash_t[t[i]] = s[i]

        return True


# @lc code=end
