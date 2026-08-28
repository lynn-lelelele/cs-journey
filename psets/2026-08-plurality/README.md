# Plurality · 2026.08.04-08.11

CS50 Problem Set 3：简单投票机。命令行传候选人，选民投票，票最多者赢。

## 状态：✅ check50 满分通过（2026.08.11）

## 运行效果

```
$ ./plurality Alice Bob Charlie
Number of voters: 3
Vote: Alice
Vote: Bob
Vote: Alice

Alice
```

## 你要写的只有两个函数

### 1️⃣ vote() —— 投票

```c
bool vote(string name)
{
    for (int i = 0; i < candidate_count; i++)   // 遍历所有候选人
    {
        if (strcmp(candidates[i].name, name) == 0)  // 票投给谁？
        {
            candidates[i].votes++;              // 找到 → 加一票
            return true;                        // 投成功，立即结束
        }
    }
    return false;                               // 没找到 → 无效票
}
```

### 2️⃣ print_winner() —— 打印赢家

```c
void print_winner(void)
{
    int max = 0;                                // 假设最高票是 0
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > max)          // 发现更高的
        {
            max = candidates[i].votes;          // 更新最高票
        }
    }
    // 以上：先找出"最高票是多少"

    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == max)         // 票数 = 最高票
        {
            printf("%s\n", candidates[i].name); // 打印（并列也打印）
        }
    }
    // 以上：再扫一遍，谁有最高票就打印谁
}
```

## 知识点

- for 循环三件套：起点 / 条件 / 每轮结束
- strcmp(a, b) == 0 判断字符串相等（不能直接 ==）
- return 立即结束函数
- 找最大值套路：max = 0 → 遍历比较 → 更新
- 并列：打印所有 == max 的人

## 踩过的坑

- print_winner 开头重复写了两遍
- 忘了第二个循环（只找 max 没打印）
- get50 不可用 → 手动建文件
- check50 要先在 submit.cs50.io 授权

## 验证

- check50 cs50/problems/2024/x/plurality → 14/14 全绿
