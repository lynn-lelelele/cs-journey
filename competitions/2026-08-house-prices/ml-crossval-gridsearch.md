# 交叉验证 + GridSearchCV · 家教笔记 · 2026.08.21

> 阶段 A：评估和调参的进阶工具 ✅

## 交叉验证（Cross Validation）

### 问题：单次切分碰运气

train_test_split 只考一次试 → 分数可能虚高/虚低。

### 交叉验证 = 考 5 次取平均

数据切 5 份，轮流当考试：
```
第1轮：训练[2345] 考[1]   第4轮：训练[1235] 考[4]
第2轮：训练[1345] 考[2]   第5轮：训练[1234] 考[5]
第3轮：训练[1245] 考[3]
```

5 个分数取平均 = 真实水平。

### 代码

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X_all, y, cv=5,
                         scoring="neg_mean_squared_error")
log_rmse = np.sqrt(-scores.mean())
```

## scoring="neg_mean_squared_error" 拆解

- mean_squared_error = 平均平方误差：每套房预测差多少（平方后平均）
- 平方的作用：负误差变正，正负不抵消，放大严重错误
- neg（负的）= sklearn 要求分数越大越好，误差越小越好 → 加负号
- 平均 = 把 1460 个误差合成"模型整体水平"（像班级平均分）

## GridSearchCV（自动调参）

### 原理

给每个参数候选值 → 自动组合成网格 → 每种组合都交叉验证 → 挑最好的

```
param_grid = {"n_estimators": [100, 300], "max_depth": [None, 10]}
→ 2×2=4 种组合 × cv 折 = 训练次数
```

### 代码

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    "n_estimators": [100, 300, 500],
    "max_depth": [None, 10, 15]
}

search = GridSearchCV(RandomForestRegressor(random_state=42),
                      param_grid, cv=5, scoring="neg_mean_squared_error")
search.fit(X_all, y)

print(search.best_params_)        # 最优参数组合
print(search.best_score_)         # 最优分数
best_model = search.best_estimator_  # 最优模型，直接用
pred = best_model.predict(test_final)
```

### 关键点

- 可以用 XGBoost：换 XGBRegressor + 换参数清单（n_estimators/learning_rate）
- param_grid = 候选值清单（键必须和模型参数名一致）
- 训练次数 = 组合数 × 折数

## 本次运行结果（House Prices）

- 最优参数：n_estimators=300, max_depth=None
- 最优 log-RMSE：0.14299（随机森林交叉验证）
- 对比：XGBoost Kaggle 成绩 0.13462（换模型更值）

## 完整工具箱

```
读数据 → 处理缺失 → 特征工程 → 交叉验证评估 → GridSearchCV 调参 → 换模型 → 提交
```
