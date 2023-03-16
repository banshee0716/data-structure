# 二元搜尋樹 Binary Search Tree

## 簡介

![Untitled](%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9%20Binary%20Search%20Tree%207190cdffb30a4178a1e66f42ca8df1f7/Untitled.png)

- 二元搜尋樹通常用於實現查詢和插入操作。因為在一個平衡的二元搜尋樹中，進行查詢和插入操作的時間複雜度可以達到 O(log n)，其中 n 為樹中節點的數量。有以下的特性

1. 以左邊節點 ( left node ) 作為根的子樹 ( sub-tree ) 的所有值都小於根節點 ( root )
2. 以右邊節點 ( right node ) 作為根的子樹 ( sub-tree ) 的所有值都大於根節點 ( root )
3. 任意節點 ( node ) 的左、右子樹也分別符合 BST 的定義
4. 不存在任何鍵值 ( key/value ) 相等的節點。

除了基本特性之外，二元搜尋樹還有其他的特點，如下：

1. 中序遍歷二元搜尋樹可以得到一個有序數列。（自己想想看怎麼跑）
2. 二元搜尋樹的高度影響著它的性能。[當二元搜尋樹極度不平衡時將會退化成為一個linked list](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)，此時查詢和插入操作的時間複雜度將退化到 O(n)。
3. 有些情況下，為了維護二元搜尋樹的平衡性，我們需要對樹進行調整。其中一種常見的調整方法是旋轉（rotation），通過左旋或右旋操作可以改變樹的結構，從而達到平衡的目的。

總之，二元搜尋樹是一種常用的數據結構，具有快速查詢和插入的優勢。在實際應用中，為了維護其平衡性，讓節點能長成一顆平衡的樹。通常會使用 AVL 樹、紅黑樹等特殊的二元搜尋樹。

## 實作

- 定義 Node 類別
    
    ```python
    class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data
    ```
    
    - 每個節點都有左右子節點和數值資料。
    - **`self.left`** 和 **`self.right`** 分別指向左子節點和右子節點。
    - **`self.data`** 存儲節點的數值資料。
    
- 定義 BinarySearchTree 類別
    
    ```python
    class BinarySearchTree:
        def __init__(self):
            self.root = None
    ```
    
    - BinarySearchTree 類別用來管理 Binary Search Tree。
    - 每個 BinarySearchTree 物件都有一個 root 屬性，用來存儲 Binary Search Tree 的根節點。
    
- 插入節點的方法
    
    ```python
    def insert(self, data):
    		new_node = Node(data)    
    		if self.root is None:
            self.root = new_node
            return
    
        current_node = self.root
        while True:
            if data < current_node.data:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                current_node = current_node.right
    ```
    
    - **`insert`** 方法用來插入一個新節點到 Binary Search Tree 中。
    - 首先創建一個新節點 **`new_node`**，並將 **`data`** 傳入 Node 類別的建構子中。
    - 如果 Binary Search Tree 是空的，將新節點作為根節點。
    - 如果 Binary Search Tree 非空，尋找新節點的插入位置。
    - 開始時，從根節點開始遍歷，如果新節點的數值比當前節點小，就繼續往左子節點移動，否則往右子節點移動，直到找到插入位置。
    - 將新節點插入到 Binary Search Tree 中。
    
- 搜尋節點的方法
    
    ```python
    def search(self, data):
    		current_node = self.root   
    		while current_node is not None:
            if current_node.data == data:
                return True
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
    
        return False
    ```
    
    - 搜尋二叉搜尋樹中是否存在一個值為 **`data`**的節點。
    - 搜尋從根節點開始，如果要查找的值比當前節點的值小，則向左子樹遞歸搜尋；
    - 如果要查找的值比當前節點的值大，則向右子樹遞歸搜尋。
    - 如果找到了該值，返回 True；否則返回 False。

- **`inorder_traversal(self, node)`**：
    - 對二叉搜尋樹進行中序遍歷，也就是從最小節點開始遍歷。
    - 中序遍歷的過程中，先遞歸遍歷左子樹，然後輸出當前節點的值，最後遞歸遍歷右子樹。
    
- **`preorder_traversal(self, node)`**：
    - 對二叉搜尋樹進行前序遍歷，也就是從根節點開始遍歷。
    - 前序遍歷的過程中，先輸出當前節點的值，然後遞歸遍歷左子樹，最後遞歸遍歷右子樹。
    
- **`postorder_traversal(self, node)`**：
    - 對二叉搜尋樹進行後序遍歷，也就是從最大節點開始遍歷
    - 後序遍歷的過程中，先遞歸遍歷左子樹，然後遞歸遍歷右子樹，最後輸出當前節點的值。
    
- `delete(self, data)`
    - 刪除節點的步驟如下：
    1.找到要刪除的節點和其父節點。
    2.根據要刪除的節點有無子節點，分為三種情況處理：
        - 要刪除的節點沒有子節點：直接將其父節點指向該節點的指標設為 None 即可。
        - 要刪除的節點只有一個子節點：將其父節點指向該節點的指標指向該節點的子節點即可。
        - 要刪除的節點有兩個子節點：需要找到其右子樹中的最小節點，將其值替換到要刪除的節點中，然後再將該最小節點刪除。
        
        3.刪除節點完成後，需要重新調整 Binary Search Tree 的結構，使其滿足 Binary Search Tree 的性質。
        

### 詳細實作

```python
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return
        
        current_node = self.root
        while True:
            if data < current_node.data:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                current_node = current_node.right

    def search(self, data):
        current_node = self.root

        while current_node is not None:
            if current_node.data == data:
                return True
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return False

    def inorder_traversal(self, node):
        if node is None:
            return

        self.inorder_traversal(node.left)
        print(node.data)
        self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node is None:
            return

        print(node.data)
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node is None:
            return

        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.data)

		def delete(self, val):
		    if self == None:
		        return self
		    if val < self.val:
		        self.left = self.left.delete(val)
		        return self
		    if val > self.val:
		        self.right = self.right.delete(val)
		        return self
		    if self.right == None:
		        return self.left
		    if self.left == None:
		        return self.right
		    min_larger_node = self.right
		    while min_larger_node.left:
		        min_larger_node = min_larger_node.left
		    self.val = min_larger_node.val
		    self.right = self.right.delete(min_larger_node.val)
		    return self

		        return True

		'''def delete(self, data):
        if self.root is None:
            return False

        # 找到要刪除的節點和其父節點
        parent_node = None
        current_node = self.root
        while current_node is not None and current_node.data != data:
            parent_node = current_node
            if data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if current_node is None:
            return False

        # 情況 1：要刪除的節點沒有子節點
        if current_node.left is None and current_node.right is None:
            if current_node != self.root:
                if parent_node.left == current_node:
                    parent_node.left = None
                else:
                    parent_node.right = None
            else:
                self.root = None

        # 情況 2：要刪除的節點只有一個子節點
        elif current_node.left is None:
            if current_node != self.root:
                if parent_node.left == current_node:
                    parent_node.left = current_node.right
                else:
                    parent_node.right = current_node.right
            else:
                self.root = current_node.right

        elif current_node.right is None:
            if current_node != self.root:
                if parent_node.left == current_node:
                    parent_node.left = current_node.left
                else:
                    parent_node.right = current_node.left
            else:
                self.root = current_node.left

        # 情況 3：要刪除的節點有兩個子節點
        else:
            # 找到要刪除節點的後繼節點和其父節點
            successor_parent_node = current_node
            successor_node = current_node.right
            while successor_node.left is not None:
                successor_parent_node = successor_node
                successor_node = successor_node.left

            # 如果後繼節點是要刪除節點的右子節點，直接刪除
            if successor_parent_node == current_node:
                successor_parent_node.right = successor_node.right
            else:
                successor_parent_node.left = successor_node.right

            # 用後繼節點取代要刪除的節點
            if current_node != self.root:
                if parent_node.left == current_node:
                    parent_node.left = successor_node
                else:
                    parent_node.right = successor_node
            else:
                self.root = successor_node

            successor_node.left = current_node.left
            successor_node.right = current_node.right

        return True
'''

# Example usage
tree = BinarySearchTree()
tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(1)
tree.insert(4)
tree.insert(7)
tree.insert(9)

print(tree.search(4)) # Output: True
print(tree.search(6)) # Output: False

tree.inorder_traversal(tree.root) # Output: 1 3 4 5 7 8 9
tree.preorder_traversal(tree.root) # Output: 5 3 1 4 8 7 9
tree.postorder_traversal(tree.root) # Output: 1 4 3 7 9 8 5
```

[資料結構大便當 — binary search tree](https://medium.com/@Kadai/資料結構大便當-binary-search-tree-3c40be3204e)

## 複雜度

| 操作 | 平均複雜度 | 最壞複雜度 |
| --- | --- | --- |
| 空間 | $O(n)$ | $O(n)$ |
| 搜索 | $O(log n)$ | $O(n)$ |
| 插入 | $O(log n)$ | $O(n)$ |
| 刪除 | $O(log n)$ | $O(n)$ |

註：n 表示 Binary Search Tree 的節點數量。最壞時間複雜度發生在當 Binary Search Tree 傾斜成單邊鍊（skewed tree）時，bst 退化為linked list。此時的搜索、插入、刪除都需要 O(n) 的時間複雜度。

### 參考資料

[資料結構大便當 — binary search tree](https://medium.com/@Kadai/資料結構大便當-binary-search-tree-3c40be3204e)

[Writing a Binary Search Tree in Python with Examples](https://blog.boot.dev/computer-science/binary-search-tree-in-python/)

[LeetCode - The World's Leading Online Programming Learning Platform](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)