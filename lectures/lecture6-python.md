# CS50 Lecture 6 · Python × Kaggle 结课笔记

> 2026.08.18-19 · 本地 Python 3.14 · [完成] L6 全部完成

## 已学清单

1. Python vs C（print / f-string / 不写类型）
2. 列表 list（[-1]、append、for 遍历）
3. 字典 dict（键值对，随便加键）
4. 列表套字典 = 数据集
5. 函数 def（不写类型）
6. pandas：DataFrame、读 CSV、选列、筛选、统计、排序
7. pandas 进阶：groupby 分组统计、缺失值处理
8. numpy：数组运算（+1、*2）、mean/max/min、筛选

## PSet 6 完成

### Mario Python（3 行，C 版 30 行）

```python
n = int(input("Height: "))
for i in range(n):
 print(" " * (n - i - 1) + "#" * (i + 1))
```

新知识：`input()` 读输入、`int()` 转换、`range(n)` 循环、字符串乘法 `"#" * 3`、字符串拼接 `+`

### Cash Python（4 行，C 版 20 行）

```python
c = int(input("Change owed: "))
coins = 0
for denom in [25, 10, 5, 1]:
 coins += c // denom
 c %= denom
print(coins)
```

新知识：`//` 整除、`%` 取余、`+=` 简写、用列表代替重复代码

## 关键语法速查

| Python | 意思 |
|--------|------|
| `input("提示")` | 读输入（C 的 get_int） |
| `int(...)` | 转数字（C 的 atoi） |
| `range(n)` | 0 到 n-1（C 的 for i<n） |
| `"#" * 3` | 字符串重复（C 做不到） |
| `a // b` | 整除（C 的 /） |
| `a % b` | 取余 |
| `+=` | 自加简写 |

## pandas 速查

```python
df["列"] # 选一列
df[["列1","列2"]] # 选多列（双括号）
df[df["列"] >= 8] # 筛选
df.head(2) # 前几行
df["列"].value_counts() # 统计
df.sort_values("列", ascending=False) # 排序
df.groupby("列")["列"].mean() # 分组平均
df.isnull().sum() # 找缺失
df["列"].fillna(df["列"].mean()) # 填缺失
```

## numpy 速查

```python
import numpy as np
arr = np.array([1, 2, 3])
arr.mean() / arr.max() / arr.min()
arr + 1 # 每个 +1
arr[arr >= 8] # 筛选
```

## 下一步

- Kaggle：House Prices 房价预测（回归赛）
- 或 CS50：L7 SQL（对数据科学有用）
