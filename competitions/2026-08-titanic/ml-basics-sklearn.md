# 机器学习入门 · 家教笔记（阶段 1 + 阶段 2）

> 2026.08.19-20 · scikit-learn 1.9.0 · Titanic 真实数据
> 阶段1：机器学习概念 [完成] 阶段2：sklearn 跑通全流程 [完成]

---

## 阶段 1：机器学习概念

### 机器学习是什么

- 传统编程：人告诉电脑规则
- 机器学习：给电脑一堆**例子**，电脑自己总结规律，然后预测新数据

### 特征 X 和标签 y（核心！）

- **特征 X = 因**（判断依据）：Pclass、Sex、Age、Fare
- **标签 y = 果**（答案）：Survived（死活）

```
例1：Pclass=3, male, 22岁, 7.25元 → 死
例2：Pclass=1, female, 38岁, 71元 → 活
```

机器学习 = 看"因→果"例子，学规律，预测新数据的果。

### 决策树 = 一串 if-else

```
 下雨吗？
 / \
 是 否
 / \
 雨大吗？ 不用带伞
 / \
 是 否
 / \
带伞 带
```

- 节点 = 一个"是/否"问题
- 叶子 = 最终结论
- 读树 = 从根一路回答，走到叶子拿答案

### 随机森林 = 100 棵树投票

- 一棵树容易学偏
- 100 棵树，每棵用不同随机子集训练，最后投票取多数
- 像问 100 个朋友意见，取多数更稳

---

## 阶段 2：sklearn 五步套路

### 完整代码

```python
# ① import（拿工具）
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# ② 准备数据（读 + 选列）
df = pd.read_csv("train.csv")
X = df[["Pclass", "Sex", "Age", "Fare"]] # 特征（因）
y = df["Survived"] # 标签（果）

# ③ 创建模型（100 棵树）
model = RandomForestClassifier(n_estimators=100)

# ④ 训练：看例子总结规律
model.fit(X, y)

# ⑤ 预测 + 评估
pred = model.predict(X)
print(accuracy_score(y, pred))
```

### 五步一句话

```
import 拿工具
X、y 准备：因 4 列 + 果 1 列
model 造模型（100 棵树）
fit 模型看例子学规律
predict 模型给预测
```

### fit 原理（训练到底在干嘛）

1. 随机抽一部分例子
2. 找一个"问题"把活/死分得最开（如"性别是女？"）
3. 分两支，每支再找下一个问题，直到每支基本只剩一种答案
4. 重复 100 次 → 100 棵树

**叶子结论 = 落到该叶子的训练样本里多数派的答案**

```
假设"女性+1/2等舱"叶子落了 30 人：25 活 5 死
→ 叶子标记"活"
```

### predict 原理（预测到底在干嘛）

**预测一个乘客 = 让他走树，走到叶子，叶子标啥预测啥**

```
新乘客：女性，2等舱，30岁
走树：女性 → 1/2等舱？是 → 年龄>2.5？是 → 落到"活"叶子
→ 预测 = 1
→ 存进 pred
```

**pred = 每行乘客一个预测结果（0/1）**，X 有 891 行 → pred 有 891 个数字。

### 最重要的坑：过拟合（开卷考试）

| 做法 | 结果 | 为什么 |
|------|------|--------|
| 不划分，fit 后直接 predict 同一批 | 98%（假） | 开卷考试，背题 |
| train_test_split 划分后 | 79.3%（真） | 考没见过的题 |

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)
accuracy_score(y_test, pred)
```

- test_size=0.2：测试集占 20%
- random_state=42：固定切法，可复现

### 真实决策树（Titanic，3 层）

```
 Sex ≤ 0.5 ?（男性？）
 / \
 是（男性） 否（女性）
 / \
 Age ≤ 6.5 ?（小孩？） Pclass ≤ 2.5 ?（1/2等舱？）
 / \ / \
 是(小孩) 否(大人) 是(1/2等舱) 否(3等舱)
 / \ / \
Pclass≤2.5? Pclass≤1.5? Age≤2.5? Fare≤23.35?
 / \ / \ / \ / \
活 死 死 死 死 活 活 死
```

规律（电脑自己总结的）：男性只有"小孩+高等舱"才活；女性 1/2 等舱基本活。

## 本次结果

- Titanic 真实准确率：79.3%（复现旧成绩 79% [完成]）

## 下一步：阶段 3 House Prices 🏠

- 回归任务（预测价格，不是分类）
- 79 个特征 → 特征工程
- 需要：Kaggle 下载 train.csv / test.csv
