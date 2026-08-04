# Plurality · 2026.08.04

CS50 Problem Set 3：简单投票机。命令行传候选人，选民投票，票最多者赢。

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

## 逐行语法讲解

### for 循环三件套

```c
for (int i = 0; i < candidate_count; i++)
    ①起点       ②条件          ③每轮结束
```
- `int i = 0` → i 从 0 开始
- `i < candidate_count` → i 没到最后一个就继续
- `i++` → 每轮结束 i + 1
- 循环体用 `{ }` 包起来

### strcmp 比较字符串

```c
strcmp(candidates[i].name, name) == 0
```
- 相等返回 0 → 用 `== 0` 判断"一样"
- 字符串**不能**用 `==` 直接比（比的是地址）

### return 两种用法

```c
return true;    // 1. 函数返回值：告诉调用者"成功了"
return false;   // 2. 也是返回值："没找到"
```
- 函数一 return 就**立即结束**，后面的代码不跑了
- `vote` 返回 bool（true/false），main 里 `if (!vote(name))` 判断是否无效票

### 找最大值套路（重要！）

```c
int max = 0;                    // 1. 先设一个"基准"
for (...)                       // 2. 遍历
    if (candidates[i].votes > max)  // 3. 发现更大的
        max = candidates[i].votes;  // 4. 更新
```
先找 max 是多少，再扫一遍打印 == max 的——这样**并列冠军**也能输出。

## 踩了什么坑

- `void print_winner(void) {` 开头重复写了两遍 → 编译报错
- 第一遍只写了找 max，忘了第二个循环打印 → 函数不输出
- 写完后没有验证并列情况

## 下次改进

- 写完函数先自查：循环是否完整、有没有漏掉输出
- 用 check50 验证：`check50 cs50/problems/2024/x/plurality`
