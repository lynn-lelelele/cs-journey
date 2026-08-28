# pandas 写代码常卡知识卡 · 2026.08.21

> House Prices 实战中遇到的 4 个高频困惑点，一次记牢。

## 1. concat + ignore_index=True（拼接重新编号）

```python
all_data = pd.concat([X, test], ignore_index=True)
```

- 拼接两张表，行号会重复（两个 0 号、两个 1 号...）
- `ignore_index=True` = 忽略旧行号，重新从 0 编号
- 类比：两个班点名册拼一起，重新编号

## 2. fillna 只填空，不动有值

```python
df["col"] = df["col"].fillna("None")
```

- 只把空（NaN）的地方填成 "None"
- 有数据的地方原样保留
- 不会全变 None！

## 3. get_dummies = 文字变 0/1 开关

```python
df = pd.get_dummies(df)
```

- 模型只认数字，"红色"没法乘，但 1/0 能乘
- 一列文字 → 每种值一列 0/1（是哪种哪列=1）
- 类比：问卷打勾

## 4. 切片冒号 [:n] / [n:]

```python
df[:1460] # 从 0 到 1459（前 1460 行）
df[1460:] # 从 1460 到结尾
```

- 冒号左边 = 起点，右边 = 终点
- 左边空 = 从开头；右边空 = 到最后

## 记忆口诀

```
concat + ignore_index = 拼接后重新编号
fillna 只填空 = 有值的别动
get_dummies = 文字变开关（1/0）
[:n] / [n:] = 前 n 个 / 从 n 到结尾
```
