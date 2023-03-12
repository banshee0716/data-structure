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

- 需要**頻繁地插入與刪除**資料。（不像Array需要騰出大量的固定空間，linked list可以輕易地通過不同的指標串聯node。)
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

## Linked List現實中的應用

1. 低級別的內存管理（Low Level Memory Management），以C語言為例：
- `malloc()`、 `free()`: 見[Heap Management](https://www.syslinux.org/wiki/index.php?title=Heap_Management)
- `chart * chart_ptr = (chart*)malloc(30);`: 取得30byte的heap memory
1. 許多Windows的應用程式：工具列視窗切換、PhotoViewer
2. [區塊鏈技術](https://c1088kiss.medium.com/%E5%8D%80%E5%A1%8A%E9%8F%88%E6%8A%80%E8%A1%93%E5%A6%82%E4%BD%95%E5%81%9A%E5%88%B0%E9%9B%A3%E4%BB%A5%E7%AB%84%E6%94%B9-%E5%B0%B1%E8%AE%93%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B8-%E5%93%88%E5%B8%8C-%E5%91%8A%E8%A8%B4%E4%BD%A0-ca1dac4cb05b)

![可以視為用hash function實作鏈結的linked list](%E9%8F%88%E7%B5%90%E4%B8%B2%E5%88%97%20Linked%20list%203fbb4410dede4b18bd03d801a461ff9c/Untitled.png)

可以視為用hash function實作鏈結的linked list

![圖源來自**[Awesome Blockchain](https://github.com/yjjnls/awesome-blockchain)，希望我不要因為這張圖被出征.......。**](%E9%8F%88%E7%B5%90%E4%B8%B2%E5%88%97%20Linked%20list%203fbb4410dede4b18bd03d801a461ff9c/Untitled%201.png)

圖源來自**[Awesome Blockchain](https://github.com/yjjnls/awesome-blockchain)，希望我不要因為這張圖被出征.......。**

## Python實作

部分實作上的使用原因：

- 選擇把操作串列的函式寫在另一個 struct 而非 Node 上有幾個原因
    1. 外部並不需知道串列內部如何實作，公開 Node 會暴露實作。
    2. 每個 Node 都帶有成員函式的話，函式指標會佔用太多額外資源。
    
    請參考以下連結
    
    [Python linked list實作](https://www.notion.so/Python-linked-list-08b441d6acd34f5b9f7e75de245e92f1)
    

[leetcode 707 design linked list](https://www.notion.so/leetcode-707-design-linked-list-a7b9bd507e0e44bcb535d4b3046c347b)

## linux核心的linked list實作

在上面的實作當中，程式碼把整個linked-list的實作分成兩個類別（class）來模擬底層操作，一個是包含了資料及指標兩個屬性的節點（class Node），另一個則是定義出各個操作的list本身（class MyLinkedList）。

但在更為貼近底層的程式語言中（擁有指標，能對記憶體直接進行操作），Linked list的節點之間通過指標連結，更為直觀。在普通的linked list實作版本中，節點通常由包含節點數據的結構體和指向下一個節點的指針組成。我們可能會創建如下的結構體：

```c
typedef struct node {
    int val;
    struct node *next;
} Node;
```

而在Linux核心中，linked list的實作方式與普通的linked list有些許不同。節點則由一個只包含指向前一個和下一個節點的指針的結構體所組成，而節點數據則保存在相鄰的數據結構中。這種設計方式稱為“container_of”。我們可能會創建如下的結構體：

```c
typedef struct list_head {
    struct list_head *prev, *next;
} ListHead;

typedef struct my_data {
    int val;
    ListHead list;
} MyData;
```

- **`list_head`**結構體代表linked list的節點，而**`my_data`**結構體則代表包含在節點中的數據。
- 在**`my_data`**結構體中，我們使用**`ListHead`**作為linked list節點的指針，而不是像在普通的linked list中使用**`Node`**結構體中的**`next`**指針。這樣，每個**`my_data`**結構體都能被轉換為一個**`list_head`**節點，而**`list_head`**節點只需包含指向前一個和下一個節點的指針。
- 這種實現方式的好處是可以降低記憶體使用量，因為節點數據被存儲在相鄰的數據結構中。此外，**`container_of`**實現還可以減少節點的指針數量，進而降低了指針的間接引用次數，提高了運行效率。
- 總體來說，Linux核心的linked list實現方式與普通的linked list相比，可以有效地減少記憶體使用量，提高運行效率，是一種更為高效的linked list實現方式。

### 相關文章

[漫談 linked list 在 linux kernel 中的不一樣](https://haogroot.com/2019/12/12/漫談-linked-list-在-linux-kernel-中的不一樣/)

[從刪除 linked-list node 看程式設計的品味](https://medium.com/fcamels-notes/從刪除-linked-list-node-看程式設計的品味-b597cc5af785)

[[你所不知道的 C 語言](https://hackmd.io/@sysprog/c-prog/): linked list 和非連續記憶體 - HackMD](https://hackmd.io/@sysprog/c-linked-list)

[linked list 和非連續記憶體操作 | Jason note](https://jasonblog.github.io/note/c/linked_list_he_fei_lian_xu_ji_yi_ti_cao_zuo.html)

## 參考資料

[單向鏈結串列 Singly linked list](https://rust-algo.club/collections/singly_linked_list/index.html#%E6%95%88%E8%83%BD)

[Rust Algorithm Club](https://rust-algo.club/collections/linked_list/index.html)

[用python實作linked-list](https://medium.com/@tobby168/%E7%94%A8python%E5%AF%A6%E4%BD%9Clinked-list-524441133d4d)