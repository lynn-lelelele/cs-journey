# CS50 Lecture 7 · SQL 入门 · 家教笔记

> 2026.08.23-24 · L7 学习中

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
SELECT 列 -- 先选列
FROM 表 -- 从哪张表
WHERE 条件 -- 再筛选
```

## SQL 基础命令（5 个，已掌握）

```sql
CREATE TABLE students (id INTEGER, name TEXT, age INTEGER, score REAL); -- 建表
INSERT INTO students (id, name, age, score) VALUES (1, 'Alice', 20, 88.5); -- 插入
SELECT name, score FROM students WHERE age < 20; -- 查 + 筛
SELECT name, score FROM students ORDER BY score DESC; -- 排序（DESC降序 ASC升序）
SELECT COUNT(*), AVG(score) FROM students; -- 统计
SELECT class, AVG(score) FROM scores GROUP BY class; -- 分组
```

### 类型 4 种

`INTEGER`（整数）`TEXT`（文字）`REAL`（小数）`BLOB`（其他）

### 注意

- 文字加单引号 `'Alice'`，数字不用
- 中文符号坑：`'Alice“` 要用英文 `'`；`<` 不是 `《`

## sqlite3 五步（Python 跑 SQL）

```python
import sqlite3
conn = sqlite3.connect("test.db") # 连接（没有自动创建）
cursor = conn.cursor() # 拿执行器
cursor.execute("SQL语句") # 执行
rows = cursor.fetchall() # 查询拿结果
conn.commit() # 插入/改后保存（空括号！）
conn.close() # 关闭
```

## JOIN（连接两张表）[重点] 2026.08.24

### 为什么需要

数据分散在多张表，要按"钥匙"拼起来：

```
students： classes：
 id name class_id id class_name
 1 Alice 1 1 A班
 2 Bob 2 2 B班
```

### 基本语法（内连接）

```sql
SELECT students.name, classes.class_name
FROM students
JOIN classes ON students.class_id = classes.id;
```

- `ON` 后面 = 连接条件（钥匙）
- 结果：两表都匹配的行

### LEFT JOIN（左表全保留）

```sql
SELECT students.name, classes.class_name
FROM students LEFT JOIN classes ON students.class_id = classes.id;
```

- 左表（FROM 后面）每一行都出现
- 右表没匹配的填 NULL

### [重点] 钥匙概念（最大的坑）

```
[完成] ON students.class_id = classes.id （学生的班级号 = 班级的编号）
❌ ON students.id = classes.id （学生号 ≠ 班级号，碰巧而已）
```

- 学生 id（学号）和班级 id（班号）是两个不同的东西
- 连接条件必须用**真正有对应关系**的字段

### 谁在左边谁全保留

| 需求 | 写法 |
|------|------|
| 所有学生（含没班级的） | `FROM students LEFT JOIN classes` |
| 所有班级（含没学生的） | `FROM classes LEFT JOIN students` |

## 进度

- [x] 数据库概念 + SQL vs pandas
- [x] 基础 5 命令 + sqlite3
- [x] JOIN 基本 + LEFT JOIN + 钥匙
- [ ] JOIN 实战练习 / L7 收尾
