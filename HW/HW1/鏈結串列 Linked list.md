# 鏈結串列 Linked list

## Introduction

- 鏈結串列是一種基本線性資料集合，每一個資料元素都是獨立的物件。儲存資料的方式和一般陣列配置連續物理記憶體空間不同，而是在各節點儲存額外的指標**指向**下一個節點。

圖例

![https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/612px-Singly-linked-list.svg.png](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/612px-Singly-linked-list.svg.png)

## 特性

鏈結串列有以下特性與優點：

- 不需事先知道資料型別大小，充分利用動態記憶體管理。
- 以常數時間插入／刪除，不需重新配置記憶體（reallocation）。

但也因動態配置記憶體等因素，連帶產生一些缺陷：

- **空間開銷大**：每個元素需儲存額外的指標空間。
- **較差的 CPU 快取**：不連續存取的特性，不利於 [CPU 快取](https://en.wikipedia.org/wiki/CPU_cache)。
- **不允許隨機存取（random access）**：搜尋特定節點仍需線性時間循序存取。

## 適用場景

- 需要頻繁地**插入與刪除**資料。（不像Array需要騰出大量的固定空間，linked list可以輕易地通過不同的指標串聯node。)
- 需要頻繁分離與合併（split and merge）資料。
- 不需要隨機存取的資料。
- 遞迴友好，因此成為大多函數式語言中基本資料型別之一。
- 教學上，常用於實作抽象資料型別，如[堆疊](https://rust-algo.club/collections/stack)與[佇列](https://rust-algo.club/collections/queue)等等。

## 名詞定義

### Node

又稱「節點」，為組成鏈結串列的基本元素，節點包含資料儲存區與指標儲存區，指標儲存區用以儲存指向其他節點位址的變數。此外，最後一個節點的不指向其他節點位址的指標成為 null pointer，慣例以 NULL 表示。

![https://rust-algo.club/collections/singly_linked_list/node-box.svg](https://rust-algo.club/collections/singly_linked_list/node-box.svg)

*（節點示意圖）*

### Head and tail

Head 為指向整個串列第一個節點的指標。而 tail 則為指向最後一個節點的指標。用 ASCII 圖表示如下：

```

   head                      tail
    |                         |
    v                         v
+--------+   +--------+   +--------+
|        |   |        |   |        |
| node 0 |-->| node 1 |-->| node 2 |--> NULL
|        |   |        |   |        |
+--------+   +--------+   +--------+

```

### Sentinel node

Sentinal node 一個特殊的節點，資料值為 NULL 的節點，用意代表鏈結串列的端點。也就是說，sentinel node 指向串列第一個節點，而串列最後一個節點也會指向 sentinel node，就像哨兵一樣守著串列前後，因而得名。

實作鏈結串列時，常常因為判斷節點是否為 NULL 而讓程式變得複雜，而 sentinel node 可減少程式操作步驟，也能增加程式可讀性。詳細資訊可以參考這篇 [NULL 與 sentinel node 的比較討論](https://stackoverflow.com/questions/5384358/)。

```

    +-----------------------------------------------+
    |                                               |
    v                                               |
+---------+   +--------+   +--------+   +--------+  |
|sentinel |   |        |   |        |   |        |  |
|         |-->| node 0 |-->| node 1 |-->| node 3 |--+
|  node   |   |        |   |        |   |        |
+---------+   +--------+   +--------+   +--------+
```

## 效能

| Operation | Complexity |
| --- | --- |
| get | $O(n)$ |
| insert | 節點已知：$O(1)$；節點未知：$O(n−i)$ |
| remove | 節點已知：$O(1)$；節點未知：$O(n−i)$ |
| append | $O(n)$ |
| prepend | $O(1)$ |
| pop first | $O(1)$ |
| pop last | $O(n)$ |
| space | $O(n)$ + 各節點額外一個指標 $n $ 個 |

> $n$：資料筆數。$i$：相對於整個容器的索引位置。
> 

值得觀察的是，許多操作因為單向鏈結串列只能從 head 開始搜索的緣故，執行時間都呈線性$O(n)$，使用上要特別注意。

## Python實作

部分實作上的使用原因：

- 選擇把操作串列的函式寫在另一個 struct 而非 Node 上有幾個原因
    1. 外部並不需知道串列內部如何實作，公開 Node 會暴露實作。
    2. 每個 Node 都帶有成員函式的話，函式指標會佔用太多額外資源。
    
    請參考以下連結
    
    [Python linked list實作](https://www.notion.so/Python-linked-list-08b441d6acd34f5b9f7e75de245e92f1)
    

### 參考資料

[單向鏈結串列 Singly linked list](https://rust-algo.club/collections/singly_linked_list/index.html#%E6%95%88%E8%83%BD)

[Rust Algorithm Club](https://rust-algo.club/collections/linked_list/index.html)

[用python實作linked-list](https://medium.com/@tobby168/%E7%94%A8python%E5%AF%A6%E4%BD%9Clinked-list-524441133d4d)