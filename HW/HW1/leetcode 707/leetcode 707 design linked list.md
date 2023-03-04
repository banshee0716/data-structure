# leetcode 707 design linked list

以下是程式碼的註解和時間/空間複雜度分析：

```python
class Node:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = None
#定義一個節點(Node)類別，具有值(val)和下一個節點的指針(nextNode)屬性。

class MyLinkedList:
    def __init__(self):
        self.head = None  # 鏈表頭節點
        self.size = 0     # 鏈表大小

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1     # 索引無效，返回 -1
        current = self.head
        for i in range(index):
            current = current.next   # 移動節點指針
        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)    # 在頭部添加元素

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)   # 在尾部添加元素

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return  # 索引無效，不添加元素
        current = self.head
        new_node = ListNode(val)
        if index <= 0:
            new_node.next = current
            self.head = new_node
        else:
            for i in range(index-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return  # 索引無效，不刪除節點
        current = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(index-1):
                current = current.next
            current.next = current.next.next
        self.size -= 1
```

- 定義一個鏈表(MyLinkedList)類別，具有鏈表頭節點(head)和鏈表大小(size)屬性。
- get()函式：根據索引(index)獲取鏈表元素，若索引無效，返回 -1。
    - 時間複雜度：O(n)，其中 n 為鏈表長度，需要遍歷 n 個節點。
    - 空間複雜度：O(1)。
- addAtHead()函式：在鏈表頭部添加元素，等價於在索引 0 的位置添加元素。
    - 時間複雜度：O(1)。
    - 空間複雜度：O(1)。
- addAtTail()函式：在鏈表尾部添加元素，等價於在索引 size 的位置添加元素。
    - 時間複雜度：O(n)
        - 需要遍歷整個鍊表，找到鏈表的最後一個節點。
    - 空間複雜度：O(1)
        - 只需要創建一個新的節點，不需要額外的空間。
    
    addAtIndex(index, val) ：再指定的index前插入節點
    
    - 時間複雜度：O(n)
        - 需要遍歷整個鏈表，找到待插入位置的前一個節點。
    - 空間複雜度：O(1)
        - 只需要創建一個新的節點，不需要額外的空間。
    
    deleteAtIndex(index) 函式的时间和空间复杂度分析：
    
    - 時間複雜度：O(n)
        - 需要遍歷整個鏈表，找到待刪除位置的前一個節點。
    - 空間複雜度：O(1)
        - 只需要修改節點的指針，不需要額外的空間。