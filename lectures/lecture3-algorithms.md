# CS50 Lecture 3 · 算法 · 2026.08.04

> 学完 Lecture 2 数组之后，这一课讲：怎么在数据里找东西、排序、衡量效率。

## 一、搜索（怎么在数组里找东西）

### 线性搜索 Linear Search（挨个找）
```
从第一个开始，一个一个往后看，找到为止。
最坏情况：n 个数要查 n 次 → O(n)
```

### 二分搜索 Binary Search（对半找）
```
前提：数组必须排好序！
每次看中间那个数，比目标大就去左半边，小就去右半边。
每次排除一半 → O(log n)
```

## 二、排序（把数组从小到大排）

| 算法 | 思路 | 效率 |
|------|------|------|
| 冒泡 Bubble | 相邻两个比，大的往后冒 | O(n²) |
| 选择 Selection | 每次找出最小的放前面 | O(n²) |
| 归并 Merge | 拆成两半各排好，再合并 | O(n log n) [重点]最快 |

## 三、大 O 表示法（衡量快慢）

只看**最坏情况**，n 越来越大时，时间怎么涨：

```
O(n²) n=100 → 10000 步 ← 慢
O(n log n) n=100 → 约 700 步
O(n) n=100 → 100 步
O(log n) n=100 → 7 步
O(1) 永远 1 步 ← 最快
```

## 四、递归 Recursion（函数调用自己）

```c
int factorial(int n)
{
 if (n == 1) return 1; // 终止条件！
 return n * factorial(n - 1); // 自己调自己
}
```

两个要素：**终止条件** + **缩小规模**。

## 五、结构体 struct（把数据打包）

```c
typedef struct
{
 string name;
 int votes;
}
candidate;
```
candidate 类型，每个变量里装着 name 和 votes。

## 六、strcmp（比较字符串）

```c
strcmp(a, b)
// 相等 → 返回 0
// a 比 b 大 → 正数
// a 比 b 小 → 负数
```

⚠️ **字符串不能直接 `==` 比较**，必须用 strcmp！因为 `==` 比的是内存地址。

## 官方资源

- 讲义：https://cs50.harvard.edu/x/2025/weeks/3/
- 视频：YouTube 搜 "CS50 2024 Week 3 Algorithms"
