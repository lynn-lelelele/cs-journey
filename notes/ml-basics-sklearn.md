# 机器学习入门 · sklearn 五步套路 · 家教笔记

> 2026.08.19 · scikit-learn 1.9.0 · Titanic 真实数据

## 机器学习是什么

- 给例子，让电脑自己总结规律，然后预测新数据
- 特征 X = 判断依据（年龄/性别/票价）
- 标签 y = 要预测的答案（是否存活）

## 决策树 / 随机森林

- 决策树 = 一连串 if-else 问题（性别？→ 年龄？→ 票价？）
- 随机森林 = 100 棵树投票（比一棵树稳）

## sklearn 五步套路（背下来！）

```python
# ① import
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# ② 数据
df = pd.read_csv("train.csv")
X = df[["Pclass", "Sex", "Age", "Fare"]].copy()   # 特征
y = df["Survived"]                                 # 标签
X["Sex"] = X["Sex"].map({"male": 0, "female": 1}) # 文字→数字
X["Age"] = X["Age"].fillna(X["Age"].mean())        # 缺失→平均

# ③ 划分训练/测试（考试题不能提前看！）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ④ 创建 + 训练
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# ⑤ 预测 + 评估
pred = model.predict(X_test)
print("准确率:", accuracy_score(y_test, pred))
```

## 最重要的坑：过拟合

- 用训练数据预测自己 → 98%（假的！开卷考试）
- 划分训练/测试后 → 79.3%（真实的！考没见过的）

## 本次结果

- Titanic 真实准确率：79.3%（复现旧成绩 79% ✅）

## 下一步

- 阶段 3：House Prices 房价预测实战（回归 + 特征工程）
