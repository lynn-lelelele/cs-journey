# CS50 Lecture 5 · 数据结构(Data Structures) · 课堂笔记

> 适用读者：已掌握 struct、指针与动态内存分配的初学者。
> 学习目标：理解链表、栈、队列与哈希表的原理与实现。

---

## 一、链表(Linked List)

### 前置知识回顾

1. struct：复合类型（"档案袋"）。
2. 指针：保存地址的变量。
3. malloc：动态内存分配。

### 自引用结构体(节点)

```c
typedef struct node
{
    int number;          // 数据域
    struct node *next;   // 指针域：指向下一个节点
}
node;
```

- `next` 是指针，因此结构体可以引用自身类型（自引用结构）。
- 内部必须写完整类型名 `struct node`，因为别名 `node` 在定义完成后才可用。

### 头插法(在链表头部插入)

```c
node *n = malloc(sizeof(node));  // 1. 分配新节点
n->number = 7;                   // 2. 写入数据
n->next = head;                  // 3. 新节点指向原链表头
head = n;                        // 4. 更新头指针
```

**顺序不能颠倒**：必须先保存原头节点，再更新头指针。

### 为什么需要链表

- 数组：连续内存，中间插入需要移动大量元素。
- 链表：节点通过指针连接，插入/删除仅需修改相邻指针。

> 应用：播放列表、浏览器历史、Ctrl+Z 撤销。

### 指针成员访问：`->`

```c
struct student *p = &s;
p->name = "lynn";       // 等价于 (*p).name = "lynn"
```

规则：结构体变量用 `.`，结构体指针用 `->`。

---

## 二、栈(Stack)：后进先出(LIFO)

> 比喻：叠盘子，后放的先拿。

```c
typedef struct
{
    int values[100];
    int top;            // 栈顶索引，初始 -1
}
stack;
```

### 入栈 push

```c
stack.top++;
stack.values[stack.top] = 3;
```

### 出栈 pop

```c
int x = stack.values[stack.top];
stack.top--;
```

要点：
- `top` 记录栈顶位置；初始 `-1` 表示空栈。
- pop 不真正删除数据，仅移动 `top`，数据会被后续覆盖。
- 应用：函数调用栈、Ctrl+Z。

---

## 三、队列(Queue)：先进先出(FIFO)

> 比喻：排队打饭，先来的先走。

```c
typedef struct
{
    int values[100];
    int front;   // 队头索引
    int rear;    // 队尾索引
}
queue;
```

初始：`front = 0`，`rear = -1`。

### 入队 enqueue

```c
queue.rear++;
queue.values[queue.rear] = 5;
```

### 出队 dequeue

```c
int x = queue.values[queue.front];
queue.front++;
```

### 栈与队列对比

| | 栈 | 队列 |
|---|---|---|
| 取出顺序 | 后进先出(LIFO) | 先进先出(FIFO) |
| 取出位置 | 栈顶 top | 队头 front |
| 新元素位置 | 栈顶 | 队尾 rear |
| 索引 | 1 个(top) | 2 个(front + rear) |

> 应用：任务调度、打印队列。

---

## 四、哈希表(Hash Table)

> 比喻：快递柜。通过哈希函数计算编号，直接定位到对应"柜子"。

### 哈希函数

```c
int hash(string s)
{
    return s[0] - 'a';   // 首字母相对 'a' 的偏移，得到 0-25
}
```

- 理想情况下，一次计算即可定位 → 时间复杂度 O(1)。
- 冲突：不同键映射到同一槽位。

### 冲突处理：链地址法(Chaining)

```c
node *table[26];   // 26 个槽位，每个槽位是一条链表
```

插入：哈希 → 定位槽位 → 链表头插。
查找：哈希 → 定位槽位 → 遍历链表。

> 哈希表 = 数组(槽位) + 链表(冲突处理)。

---

## 术语表

| 术语 | 含义 |
|---|---|
| 节点(Node) | 链表的基本单元 |
| 自引用结构体 | 结构体内含指向自身类型的指针 |
| 头插法 | 在链表头部插入新节点 |
| LIFO / FIFO | 后进先出 / 先进先出 |
| 哈希函数 | 将键映射为槽位编号的函数 |
| 冲突 | 不同键映射到同一槽位 |
| 链地址法 | 用链表解决哈希冲突 |

## 一句话总结

- 链表 = 手拉手的节点，增删灵活。
- 栈 = 叠盘子，后进先出。
- 队列 = 排队，先进先出。
- 哈希表 = 数组 + 链表，理想 O(1)。
