# House Prices · 阶段 3.1 基线 · 家教笔记

> 2026.08.21 · Kaggle 房价预测（回归赛）· 第一个基线 ✅

## 目标

预测 1459 套房子的成交价（回归任务，不是分类）。

## 数据

- train.csv：1460 行 × 81 列（80 特征 + SalePrice 房价）
- test.csv：1459 行 × 80 列（没房价，要预测）
- data_description.txt：79 个特征说明
- sample_submission.csv：提交模板

## 完整流程（5 步）

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# ① 读数据 + 分 X/y
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
y = train["SalePrice"]                 # 标签：房价
X = train.drop(columns=["SalePrice"])  # 特征：去掉房价

# ② 拼接 + 统一填缺失（保证训练/测试处理一致）
all_data = pd.concat([X, test], ignore_index=True)
for col in all_data.columns:
    if pd.api.types.is_numeric_dtype(all_data[col]):
        all_data[col] = all_data[col].fillna(all_data[col].median())  # 数值填中位数
    else:
        all_data[col] = all_data[col].fillna("None")                  # 文字填 None

# ③ 文字转数字（0/1 开关）
all_data = pd.get_dummies(all_data)

# ④ 拆回训练/测试
X = all_data[:len(train)]
test_final = all_data[len(train):]

# ⑤ 训练 + 预测
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)
pred = model.predict(test_final)
```

## 关键知识点

- **Regressor vs Classifier**：预测数字用 Regressor，预测 0/1 用 Classifier
- **pd.concat + ignore_index=True**：拼接时重新编号，避免行号重复
- **fillna 只填空**：有数据的地方不动
- **get_dummies**：文字 → 多列 0/1（哪种哪列=1），模型才能做数学运算
- **缺失 ≠ 坏事**：PoolQC 缺失 = 没泳池（填 "None" 表示没有）
- **is_numeric_dtype 判断**：pandas 3.x 判断列类型要用它，不能用 dtype == "object"

## 成绩

- Kaggle 提交分数：**0.14758**（RMSE，越低越好）
- 水平：中等偏上基线（顶级 ~0.11，新手常见 0.16+）

## 遇到的问题与坑

1. **Kaggle 下载**：要先 Join Competition（接受规则）才能下载数据；Download All 会弹 kagglehub 代码框，直接用网页下载按钮即可
2. **pandas 3.x 类型判断坑**：`dtype == "object"` 对文字列失效 → 报 `Cannot perform reduction 'median' with string dtype` → 改用 `pd.api.types.is_numeric_dtype()`
3. **首次 import sklearn 慢**：第一次要初始化，超时正常，第二次就快

## 下一步（冲分）

- 特征工程：总面积 = 各面积之和、合并稀有类别
- 调参：n_estimators、max_depth
- 换模型：XGBoost

## 状态

- [x] 3.1 读数据 + 基线提交（0.14758）
- [ ] 3.2 特征工程
- [ ] 3.3 调参冲分
