# CS50 Lecture 6 · Python × Kaggle 结合课 · 家教笔记

> 2026.08.18-19 开始 · 本地 Python 3.14 环境（不用联网！）

## 目标

CS50 L6 Python + Kaggle 数据分析一起学，每课用真实数据场景。

## 第 1 课：Python vs C

| | C | Python |
|---|-----|--------|
| 打印 | `printf("Hello!\n")` | `print("Hello!")` |
| 变量 | `int n = 5;` | `n = 5`（不写类型） |
| 数组 | `int arr[3]` | `arr = [1,2,3]`（自动扩容） |
| 指针/malloc | 要手动 | 不存在！ |

第一个程序：
```python
movie = "Inception"
rating = 8.8
print(f"{movie} 评分 {rating}")   # f-string 直接塞变量
```

坑：中文引号 `“”` vs 英文 `"` → SyntaxError

## 第 2 课：列表 list

```python
ratings = [8.8, 7.5, 9.2, 6.8, 8.1]

ratings[0]      # 第一个：8.8
ratings[-1]     # 最后一个：8.1（C 没有负数索引！）
len(ratings)    # 长度：5
ratings.append(7.7)   # 末尾加一个（C 数组做不到）
```

遍历（不用下标）：
```python
for r in ratings:
    print(r)
```

求平均：
```python
total = 0
for r in ratings:
    total = total + r
avg = total / len(ratings)
```

## 第 3 课：字典 dict（像 C struct 但更灵活）

```python
movie = {
    "title": "Inception",
    "rating": 8.8,
    "year": 2010,
    "genre": "Sci-Fi"
}

movie["title"]          # 拿值：Inception
movie["rating"] = 9.0   # 改值
movie["director"] = "Nolan"   # 加新键（C 做不到！）
```

比喻：名片，`movie["键"]` = 看/改名片上那一栏。

## 第 4 课：列表套字典 = 数据集（Kaggle 核心！）

```python
movies = [
    {"title": "Inception", "rating": 8.8},
    {"title": "Titanic",   "rating": 7.9},
    {"title": "Avatar",    "rating": 7.9}
]

for m in movies:
    print(m["title"])          # 遍历所有

for m in movies:
    if m["rating"] >= 8.0:     # 条件筛选
        print(m["title"])
```

Kaggle 表格 = 列表（行）+ 字典（每行）。

## 第 5 课：函数

```python
def average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total / len(numbers)

print(average(ratings))   # 复用！
```

| C | Python |
|---|--------|
| `bool vote(string name)` | `def vote(name):`（不写类型） |
| `{}` 包代码 | 缩进 4 空格 |

## 第 6 课：pandas 基础 ✅

pandas 3.0.5 已装。DataFrame = 一整张 Excel 表。

### 创建表格

```python
import pandas as pd

movies = pd.DataFrame({
    "title":  ["Inception", "Titanic"],
    "rating": [8.8, 7.9],
    "year":   [2010, 1997]
})
```

### 核心操作（Kaggle 基本功）

```python
movies["title"]                      # 选一列
movies[["title", "year"]]            # 选多列（双括号 = 传列表）
movies[movies["rating"] >= 8.0]      # 筛选：评分 >= 8 的行
movies.head(2)                       # 只看前 2 行
```

### 读 CSV 文件（Kaggle 数据入口）⭐

```python
movies = pd.read_csv("C:/Users/19918/Desktop/movies.csv")
print(movies)                        # 整张表
print(movies["genre"].value_counts()) # 统计每种类型数量
```

### 双括号原理

```python
movies[["title", "year"]]  # 里面的括号 = 列名列表，外面 = 访问 movies
movies["title"]            # 单列用单括号
```

### 筛选原理

```python
movies[movies["rating"] >= 8.0]
# ① movies["rating"] >= 8.0 → 一串 True/False
# ② movies[True/False列表] → 只保留 True 的行
```

## 本地文件（桌面）

hello.py / ratings.py / avg.py / movie.py / movies.py / average.py / pandas1.py / pandas2.py / pandas3.py / movies.csv

## 进度

- CS50：L1-L5 ✅，L6 Python 进行中
- Kaggle：Python 基础 ✅ → pandas 基础 ✅ → 下一步：排序/分组/缺失值 → sklearn → 打比赛
