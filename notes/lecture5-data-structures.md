# CS50 Lecture 5 · 数据结构 · 家教课堂笔记（第1课：链表）

> 2026.08.14 一对一辅导 · 已学：链表基础

## 前置知识（这课要用）

1. struct = 打包（档案袋）：`s.name = "lynn"`
2. 指针 = 存地址：`int *p = &n; *p = 99`
3. malloc = 借内存：`int *p = malloc(sizeof(int))`

## 新知识 1：struct 里能放指针

```c
struct box { int number; int *next; };
```
档案袋里可以放纸条（地址）。

## 新知识 2：-> 运算符

```c
struct student s;
struct student *p = &s;
p->name = "lynn";     // 等价于 (*p).name = "lynn"
```

口诀：结构体变量用 `.`，结构体指针用 `->`。

## 新知识 3：链表节点（自引用）

```c
typedef struct node
{
    int number;          // 数据
    struct node *next;   // 指向下一个节点
}
node;
```

- `next` 是指针，**不需要知道对方完整大小**，所以可以指向自己类型（不矛盾）
- 里面必须写 `struct node`（大名），因为小名 `node` 要等定义完才生效

## 新知识 4：头插入（造 → 装 → 挂 → 换头）

```c
node *n = malloc(sizeof(node));  // ① 造新车厢
n->number = 7;                   // ② 装货
n->next = head;                  // ③ 挂住原来第一名
head = n;                        // ④ 名单更新，新节点当第一名
```

顺序不能反：**先记住原来的第一名，再换头**，否则队伍断掉。

## 为什么需要链表（对比数组）

- 数组 = 固定座位，中间插入要全部挪动
- 链表 = 排队，插队只改前后两个指针

## 现实应用

- 网易云歌单（下一首/上一首）
- 相册左右滑动
- Ctrl+Z 撤销历史
- 浏览器后退
- 火车车厢

## 一句话

**链表 = 手拉手的节点，数据经常变（加/删/插）就用它。**
