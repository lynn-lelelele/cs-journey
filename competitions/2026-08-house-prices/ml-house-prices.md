# Kaggle 实战 · House Prices 房价预测 · 课堂笔记

> 适用读者：掌握 sklearn 基础流程的初学者。
> 竞赛：Kaggle House Prices（回归任务，评价指标为 RMSE 对数）。

## 最终成绩：0.13462

| 版本 | Kaggle 分数 | 说明 |
|------|------------|------|
| 基线：随机森林 100 棵 | 0.14758 | 全流程跑通 |
| + 特征工程 3 个 | 0.14221 | TotalSF/HouseAge/QualSF |
| + XGBoost 300 棵 | **0.13462** | 一棵补一棵的错 |

## 阶段 3.1：基线（0.14758）

- 读数据 → 填缺失 → get_dummies → 随机森林 → 提交
- 踩坑：Kaggle 要 Join；pandas 3.x 用 is_numeric_dtype

## 阶段 3.2：特征工程（0.14221）

### 特征工程 3 问
1. 同一件事拆开存？→ 加（总面积）
2. 时间点相减有意义？→ 减（房龄）
3. 组合起来更强？→ 乘（质量×面积）

```python
for df in [X, test]:
 df["TotalSF"] = df["1stFlrSF"] + df["2ndFlrSF"] + df["TotalBsmtSF"]
 df["HouseAge"] = df["YrSold"] - df["YearBuilt"]
 df["QualSF"] = df["OverallQual"] * df["TotalSF"]
```

- 让模型自动学（浴室权重）比人工猜更好

## 阶段 3.3：调参 + XGBoost（0.13462）

### 调参
```python
RandomForestRegressor(n_estimators=300, max_depth=15)
```
- 树数量/深度是旋钮，但不是乱调就好，要试组合

### XGBoost = 一棵补一棵的错

```
树1 学房价 → 算残差(真实-预测) → 树2 学残差 → 新残差 → 树3 学...
最终 = 所有树加起来
```

- 类比：考试只复习错题；射箭每箭修正偏差
- 随机森林 = 独立投票；XGBoost = 接力补错

### 换模型只改 2 行

```python
from xgboost import XGBRegressor
model = XGBRegressor(n_estimators=300, learning_rate=0.05, random_state=42)
# fit / predict 写法完全不变！
```

### learning_rate
- 每棵树学多快（0.05 慢但稳，0.3 快但易冲过头）

## 学到的完整比赛流程

```
下载 → 探索 → 填缺失 → get_dummies → 特征工程 → 换模型 → 提交
```

## 下一步

- 可以打新比赛（如 Playground 系列周赛）
- 或学更多：交叉验证、超参搜索（GridSearchCV）、深度学习
