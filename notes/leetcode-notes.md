# LeetCode 刷题笔记 · 2026.08.24 开始

> 目标：每周 3-5 题，面试/进组打底

## 第 1 题：Two Sum（两数之和）⭐ 面试必考

### 题面

给数组 nums 和目标 target，找出哪两个数相加等于 target，返回它们的下标。

```
nums = [2, 7, 11, 15], target = 9
→ [0, 1]（2 + 7 = 9）
```

### 暴力解（两层循环，O(n²)）

```python
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []    # 兜底：找不到返回空列表
```

### 关键点

- `range(len(nums))` = 生成下标（0 到 长度-1）
- `nums[i]` = 第 i 个位置的值
- `j` 从 `i+1` 开始 = 避免自己和自己配对、避免重复
- 比较用 `==`（不是 `=`）
- def/for/if 行尾都要冒号

### 兜底（边界情况）⭐ 真实编程思维

- LeetCode 题目保证有解，但不写兜底过测试也能过
- 真实世界数据不可靠，**必须处理"找不到"的情况**
- 找不到 → 返回空列表 `[]`（比 None 安全，调用方好判断）

### 复杂度

- 暴力解 O(n²)：两层循环，数据大了会慢
- 进阶：哈希表 O(n)（以后学）

## 踩过的坑

- 忘了冒号（def/for/if）
- `=` 写成 `==`（比较）
- 返回了值而不是下标（要用 range 遍历下标）
