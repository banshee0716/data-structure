class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed) -> bool:
            # 計算以速度 speed 吃掉所有香蕉需要的時間是否小於等於 h 小時
            return sum((pile - 1) // speed + 1 for pile in piles) <= h

        # 香蕉數量的上限是總堆數中的最大值
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                # 以當前速度吃完所有香蕉需要的時間小於等於 H 小時，縮小速度範圍
                right = mid
            else:
                # 以當前速度吃完所有香蕉需要的時間大於 H 小時，增大速度範圍
                left = mid + 1

        return left


"""
時間複雜度：二分查找需要 log(max(piles)) 次，每次查找需要 O(n) 時間（其中n是堆數量），因此總時間複雜度為 O(nlog max(piles))。

空間複雜度：除了輸入和輸出的空間外，這個函數使用的額外空間是常數級別的，因此空間複雜度為 O(1)。
"""
