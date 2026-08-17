# CS50 Lecture 5 · 数据结构 · 家教课堂笔记

> 2026.08.14-18 一对一辅导
> ✅ 第1课：链表基础
> ✅ 第2课：栈 Stack + 队列 Queue

---

## 第 1 课：链表 Linked List

### 前置知识

1. struct = 打包（档案袋）：`s.name = "lynn"`
2. 指针 = 存地址：`int *p = &n; *p = 99`
3. malloc = 借内存：`int *p = malloc(sizeof(int))`

### struct 里能放指针

```c
struct box { int number; int *next; };
```
档案袋里可以放纸条（地址）。

### -> 运算符

```c
struct student *p = &s;
p->name = "lynn";     // 等价于 (*p).name = "lynn"
```
口诀：结构体变量用 `.`，结构体指针用 `->`。

### 链表节点（自引用）

```c
typedef struct node
{
    int number;          // 数据
    struct node *next;   // 指向下一个节点
}
node;
```

- `next` 是指针，不需要知道对方完整大小，所以可以指向自己类型
- 里面必须写 `struct node`（大名），因为小名 `node` 要等定义完才生效

### 头插入（造 → 装 → 挂 → 换头）

```c
node *n = malloc(sizeof(node));  // ① 造新车厢
n->number = 7;                   // ② 装货
n->next = head;                  // ③ 挂住原来第一名
head = n;                        // ④ 名单更新
```

顺序不能反：**先记住原来的第一名，再换头**。

### 为什么需要链表

- 数组 = 固定座位，中间插入要全部挪动
- 链表 = 排队，插队只改前后两个指针
- 应用：歌单下一首、相册滑动、Ctrl+Z、浏览器后退

---

## 第 2 课：栈 Stack（后进先出 LIFO）

**比喻：叠盘子**，后放的先拿。

```c
typedef struct
{
    int values[100];   // 盘子架（100 层）
    int top;           // 最上面的层号（初始 -1）
}
stack;
```

### push（放盘子）

```c
stack.top++;                    // 指示器升一层
stack.values[stack.top] = 3;    // 放上去
```

### pop（拿盘子）

```c
int x = stack.values[stack.top];   // 拿最上面
stack.top--;                       // 指示器降一层
```

### 关键理解

- `top` = 最上面盘子的**层号**（-1 表示一个都没有）
- pop **不是删除**，只是降 top，数据留着下次覆盖
- 数组索引从 0 开始 → 初始 top = -1，+1 后正好 0

### 追踪练习（已掌握）

```
push 1、2、3 → 栈 [1,2,3]，top=2
pop 一次     → 拿 3，top=1
pop 两次     → 拿 2、1，栈空
```

---

## 第 3 课：队列 Queue（先进先出 FIFO）

**比喻：排队打饭**，先来的先走。

```c
typedef struct
{
    int values[100];   // 队伍位置
    int front;         // 队头（先走的）
    int rear;          // 队尾（新来的站这）
}
queue;
```

初始：`front = 0`，`rear = -1`

### enqueue（入队：站队尾）

```c
queue.rear++;                    // 队尾往后挪
queue.values[queue.rear] = 5;    // 新来的站最后
```

### dequeue（出队：队头走）

```c
int x = queue.values[queue.front];   // 队头的人拿走
queue.front++;                       // 队头往后挪
```

### 对比

| | 栈 | 队列 |
|---|-----|------|
| 拿走谁 | 最后进来的（top） | 最前面的（front） |
| 新来的站哪 | 最上面 | 最后面 |
| 指针 | 一个 top | 两个：front + rear |

## 一句话总结

- 链表 = 手拉手的节点，灵活增删
- 栈 = 叠盘子，后进先出（Ctrl+Z）
- 队列 = 排队，先进先出（打印任务）
