# House Prices · 阶段 3 笔记

> 2026.08.21 · Kaggle 房价预测（回归赛）

## 阶段 3.1：基线 ✅

- 全流程：读数据 → 填缺失 → get_dummies → 随机森林回归 → 提交
- 基线分数：**0.14758**
- 踩坑：Kaggle 要先 Join Competition；pandas 3.x 用 is_numeric_dtype 判断列类型

## 阶段 3.2：特征工程 ✅

### 判断逻辑（3 问）

1. **同一件事被拆开存？** → 加（1楼+2楼+地下室 = 总面积）
2. **时间点相减有意义？** → 减（卖房年 - 建房年 = 房龄）
3. **组合起来信号更强？** → 乘（质量×面积 = 又大又好）

### 用到的 3 个新特征

```python
for df in [X, test]:
    df["TotalSF"] = df["1stFlrSF"] + df["2ndFlrSF"] + df["TotalBsmtSF"]
    df["HouseAge"] = df["YrSold"] - df["YearBuilt"]
    df["QualSF"] = df["OverallQual"] * df["TotalSF"]
```

### 让模型自动学（关键决策）

- 浴室列（FullBath/HalfBath/BsmtFullBath/BsmtHalfBath）**不人工合并**
- 让随机森林自己学权重 → 比人工猜权重更好！

### 结果对比（同口径本地评估）

| 版本 | 分数 |
|------|------|
| 无特征工程 | 0.15498 |
| 4 特征（人工浴室权重） | 0.15142 |
| 3 特征（浴室让模型学） | 0.15001 |

### Kaggle 真实分数

- 基线：0.14758
- 特征工程版：**0.14221** ✅ 提升 0.005

### 相乘特征逻辑

- 乘 = 捕捉协同效应（两个因素同时大 → 效果翻倍）
- 例：质量×面积、曝光×点击率、价格×折扣

## 阶段 3.3：调参 / XGBoost（下一步）

- [ ] 调参：n_estimators、max_depth
- [ ] XGBoost（比赛神器）
