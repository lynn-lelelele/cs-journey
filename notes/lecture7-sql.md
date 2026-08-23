# CS50 Lecture 7 · SQL 入门 · 家教笔记

> 2026.08.23 开始 · 第 1-2 小点

## 数据库是啥

- 数据库 = 专门存数据的"超级表格仓库"
- SQL = 和数据库对话的语言

### 数据库 vs Excel

| | Excel | 数据库（SQL） |
|---|-------|--------------|
| 数据量 | 几万行就卡 | 几百万行流畅 |
| 多人同时 | 会乱 | 几百人同时 OK |
| 查询 | 慢慢点 | 一句话问出来 |
| 权限 | 无 | 可控制 |

## SQL 和 pandas 对应表（核心！）

| pandas（会了） | SQL |
|----------------|-----|
| `df[df["age"] > 18]`（筛选） | `SELECT * FROM students WHERE age > 18` |
| `df["name"]`（选一列） | `SELECT name FROM students` |
| `df.sort_values("age")`（排序） | `SELECT * FROM students ORDER BY age` |
| `df.groupby("class").mean()`（分组） | `SELECT class, AVG(score) FROM students GROUP BY class` |

### SQL 语法顺序（和 pandas 不同）

```sql
SELECT 列   -- 先选列
FROM 表     -- 从哪张表
WHERE 条件  -- 再筛选
```

## pandas 四个操作复习

### 1. 筛选

```python
df[df["age"] > 18]    # df[条件] → True/False 选行
```

### 2. 选列

```python
df["name"]              # 一列
df[["name", "age"]]     # 多列（双括号！）
```

### 3. 排序

```python
df.sort_values("age")                  # 默认升序
df.sort_values("age", ascending=False) # 降序
```

### 4. 分组统计

```python
df.groupby("class")["score"].mean()
# ① 按班级分组 ② 看score列 ③ 算平均
```

## 记忆口诀

```
df[条件]      → WHERE
df["列"]      → SELECT 列
sort_values   → ORDER BY
groupby+mean  → GROUP BY + AVG
```
