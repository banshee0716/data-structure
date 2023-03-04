# 前綴和 Prefix sum

## Introduction

- 也被稱為cumulative sum (累計和)。在 prefix sum 中，第i個元素是原始數組前i個元素的總和。也就是說，如果原始數組為a，那麼 prefix sum數組為s，其中 s[i] = a[0] + a[1] + ... + a[i-1]。
- 可以在O(n)的時間複雜度內，計算出一個數組中所有前綴子數組的和，並將結果存儲在另一個數組中。是一種典型的**用空間換時間**的演算法
- prefix sum 最常見的用途之一是在**求解區間和**的問題中。如果我們需要求出原始數組a的某一個區間[l,r]的和，只需要計算 prefix sum數組 s[r+1] - s[l] 即可。這是因為 `s[r+1]` 包含了 a[0] 到a[r] 的和，而 s[l] 包含了 a[0] 到a[l-1]的和，因此 s[r+1] - s[l] 就是區間 [l,r] 的和。
- prefix sum 還可以用來優化某些計算，例如在計算數組中每個元素的前綴平均值時，只需要計算出 prefix sum 數組，然後通過 s[i] / i 計算出前 i 個元素的平均值。

## 實作

1. 創建一個與原始數組相同大小的數組prefix_sum，並將其第一個元素設為原始數組的第一個元素。
2. 通過迭代原始數組的每個元素，計算當前元素和前一個元素之和，並將其存儲在prefix_sum數組中。具體地，對於原始數組中的每個元素nums[i]，prefix_sum[i]等於prefix_sum[i-1]加上nums[i]。
3. 返回prefix_sum數組作為結果。

以下是Python的代碼實現：

```python
def prefix_sum(nums):
    n = len(nums)
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + nums[i]

    return prefix_sum
```

例如，對於以下輸入：

```
nums = [1, 2, 3, 4, 5]
```

prefix_sum演算法將返回以下輸出：

```
[1, 3, 6, 10, 15]
```

這是由原始數組[1, 2, 3, 4, 5]計算而來的，其中第一個元素1等於原始數組的第一個元素，後續元素依次為s[1]=1+2=3、s[2]=1+2+3=6、s[3]=1+2+3+4=10、s[4]=1+2+3+4+5=15。

## 效能

| Operation | Complexity |
| --- | --- |
| Scan | $O(n)$ |
| space | $O(n)$ |

<aside>
💡 Prefix Sum的時間複雜度為O(n)，其中n為原始數組的大小，因為算法只需要遍歷一次原始數組。空間複雜度為O(n)，因為需要額外創建一個prefix_sum數組來存儲計算結果。

</aside>