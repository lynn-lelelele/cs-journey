# ML 实战 3 · S6E8 手机成瘾预测 — 从 0.962 到 0.97082

> 适用读者：理解交叉验证与基础集成概念的初学者。
> 竞赛：Kaggle Playground S6E8（二分类，评价指标 AUC）。
> 最终成绩：OOF 0.96966 → 公共榜 0.97082。

---

## 1. 这场比赛在干嘛

- 预测一个人会不会"手机成瘾"（二分类：0/1）
- 数据：train 691,369 行 × 14 列，test 296,302 行
- 评分：**AUC**（曲线下面积，越大越好，0.5=瞎猜，1=完美）
- 正样本比例：70.9%（有点不平衡）

特征（14 列里 13 个是输入）：
- 数值（9 个）：age、daily_screen_time_hours、social_media_hours、gaming_hours、work_study_hours、sleep_hours、notifications_per_day、app_opens_per_day、weekend_screen_time
- 文字（3 个）：gender、stress_level、academic_work_impact

---

## 2. 战斗记录（按时间）

### 阶段 1：自己训练（单模型天花板 ~0.963）

| 尝试 | OOF AUC |
|---|---|
| LGBM + 分类列目标编码 | 0.96257 → 0.96329 |
| + 缺失值模式特征 | 0.96354 |
| + 数值列目标编码 | 0.96310（更差！）|
| + 交互特征（比值/和/差） | 0.96246（更差！）|
| kNN 单独 | 0.92424（太弱）|

**关键发现（EDA）**：
- 分类列几乎没信息！gender/stress/impact 的标签均值只差 0.01
- 真正的信号全在数值列：daily_screen(0.61)、weekend_screen(0.59)、social(0.53)
- 9 个数值列组合才到 0.963，单列只有 0.871 → 信号藏在多列交互里
- 但 LGBM 自己就能学交互，显式造交互特征反而稀释

### 阶段 2：自己堆叠（上限 ~0.964）

- 自己训了 7 个模型（LGBM×3 seed、XGB×2 seed、缺失版、dummy 版），全部 OOF
- LR / LGBM / 权重搜索做元模型
- 最优：**0.96391**（还是不够）

**撞墙结论**：单靠"自己调参 + 堆叠"到不了 0.97，单模型信息量就这么多。

### 阶段 3：社区 74 模型 OOF 库（突破！）

- 发现高分方案全在用公开的 **"S6E8 full OOF library"**（Szymon Kłapiński 发布，CC0 许可）
- 74 个模型，全部用**同一个 CV 方案** `StratifiedKFold(5, shuffle=True, random_state=42)`，按行对齐
- 最强单模型：naji03/naji05 OOF 0.96881（作者私模）
- 我的最终方案：**logit 变换 + LogisticRegression 堆叠 74 个 OOF**

```
输入：74 列 OOF 概率（每列一个模型的"干净预测"）
 → logit 变换（把 0~1 概率展开到 -∞~+∞）
 → 逻辑回归当裁判（学每个模型权重）
 → 输出：最终预测
```

**结果：OOF 0.96966 → 公共榜 0.97082** [完成]（比 README 声称的 0.96943/0.97062 还高）

---

## 3. 核心知识点（今天学会的）

### 3.1 什么是 OOF（Out-of-Fold）

5 折交叉验证的"副产品"：

```python
skf = StratifiedKFold(5, shuffle=True, random_state=42)
oof = np.zeros(len(train)) # 空箱子，装 69 万个预测
for tr_idx, va_idx in skf.split(X, y):
 model.fit(X[tr_idx], y[tr_idx]) # 4/5 训练
 oof[va_idx] = model.predict_proba(X[va_idx])[:, 1] # 1/5 预测，存进箱子
```

跑完 5 轮，**每一行都恰好当过 1 次"考生"**，留下的预测就是 OOF。
- 每个预测都是模型**没见过这个样本**时做的 → 真实水平
- 所以能安全地喂给下一层模型（不泄漏答案）

### 3.2 如何保证"没偷看"？

关键：`skf.split` 返回的 **tr_idx 和 va_idx 永远不重叠**。
- `fit(X[tr_idx], y[tr_idx])` 只吃训练索引 → 验证集的数据根本没进 fit
- 不是"尽量没学"，是**机制上不可能学**——验证行的 X 和 y 都被索引挡住了

### 3.3 StratifiedKFold 分层怎么实现？

- 先把正样本（成瘾）均匀切成 5 堆，再把负样本均匀切成 5 堆
- 每折 = 1 堆正 + 1 堆负 → 每折比例都 ≈ 70.9%，代表整体
- 看 y 的是**切分器**，不是模型 → 模型依然没偷看

### 3.4 为什么用 logit + 逻辑回归当裁判？

- 74 个模型的预测高度相关（0.987~0.999），直接平均浪费信息
- LR 学的是"每个模型该信多少"，还能在 logit 空间（展开极端值）里更好区分
- 试过 LGBM 当裁判 → 0.96942，更差（太复杂，过拟合）
- 试过 rank 变换 → 0.96962，更差
- **简单 LR 就是最好的裁判**

### 3.5 为什么 74 个考官拼起来 > 最强考官？

- 最强单模型 0.96881，全拼起来 0.96966（+0.00085）
- 靠的是**多样性**：模型之间相关度越低，互补越多
- 例：lookup（查表 Transformer）和所有人相关度最低（0.9869），单独加它就值 +0.0001

### 3.6 诚实分数 vs 过拟合公共榜（重要！）

- 诚实方案：OOF ≈ 公共榜（差 0.001 以内），我们 0.96966 → 0.97082 [完成]
- 公共榜 0.97110 以上：基本是**过拟合公共榜**（反复提交试探测试集噪声）
- 证据：rayk 自己标题《Why Every S6E8 Notebook Above 0.97110 Overfits》；najiama 的提交文件叫 `20_No_OOF_Useless_Overfitting_submission.csv`
- **真实能力不涨，换数据立刻现形** → 不学这种玩法

---

## 4. 复现代码

```python
import numpy as np, pandas as pd, glob, os
from scipy.special import logit
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score

L = "path/to/s6e8-oof-library/oof"
keys = pd.read_parquet("path/to/train_keys.parquet")
y = keys["addicted_label"].values

names = sorted(os.path.basename(p)[4:-4] for p in glob.glob(f"{L}/oof_*.npy"))
O = np.column_stack([np.load(f"{L}/oof_{n}.npy") for n in names]).astype("float64")
T = np.column_stack([np.load(f"{L}/test_{n}.npy") for n in names]).astype("float64")
OL, TL = logit(np.clip(O, 1e-6, 1-1e-6)), logit(np.clip(T, 1e-6, 1-1e-6))

skf = StratifiedKFold(5, shuffle=True, random_state=42)
oof = np.zeros(len(y))
for itr, iva in skf.split(OL, y):
 oof[iva] = LogisticRegression(max_iter=3000).fit(OL[itr], y[itr]).predict_proba(OL[iva])[:, 1]
print("blend OOF AUC:", roc_auc_score(y, oof)) # 0.96966
```

---

## 5. 踩坑记录

1. **XGB 的 fit 没有 callbacks 参数**（那是 LGBM 的）→ 按模型类型分派
2. **Windows 控制台 GBK 编码** → 打印中文/emoji 报错，设 `PYTHONIOENCODING=utf-8`
3. **读 parquet 需要 pyarrow** → `pip install pyarrow`
4. **浏览器登录墙** → Kaggle 代码/数据集要登录才能看，让用户浏览器下载最稳
5. **自己训的 7 个 OOF 拼进 74 库没用**（相关度太高，加 0）→ 相关度比强度更重要

---

## 6. 下一步

- [ ] 学 rayk 的 transductive 信号（+0.0003，边际效益小，先放着）
- [ ] 自己从零训一个能到 0.97 的模型（真正的能力）
- [ ] 上传笔记到 GitHub [完成] 本次完成

---

## 7. 课后复习 · OOF 三课(8-26 讲透版)

### 一句话理解 OOF
> OOF = 训练集里的每个人,在被"假装从没学过"的模型预测时,得到的那个预测值。

### 走查:6 人切 2 折
- 第 1 折:训练 3/4/5 号 → 预测 0/1/2 号,存 oof[0], oof[1], oof[2]
- 第 2 折:训练 0/1/2 号 → 预测 3/4/5 号,存 oof[3], oof[4], oof[5]
- 每个 oof 值都是"模型第一次见这个人"时的判断 → 真实水平

### 三个铁律
1. **没偷看靠机制**:`fit(X[tr_idx], y[tr_idx])` 只吃训练索引,验证集的数据被索引挡住,不可能进模型
2. **分层≠偷看**:看 y 的是切分器(只为了分组公平),不是模型;分层保证每折比例≈整体(70.9%)
3. **相关度 > 强度**:集成赚的是"错得不一样"的钱;相关度=两个考官看法同步的程度;越不相关越互补
 - 例:19 个 LGBM 相关 0.99+(复读机);lookup 相关 0.9869(全场最低)→ 单独加它最值钱
 - 例:自己训的 7 个模型拼进 74 库 = 0 提升(和库里高度同步)

### 为什么裁判用 logit + LR
- 74 列高度相关(0.987~0.999),直接平均浪费信息
- LR 学"每个模型该信多少",logit 把 0~1 概率展开到实数域,更好区分极端值
- 试过 LGBM 当裁判(0.96942)、rank 变换(0.96962)→ 都更差,简单 LR 最优
