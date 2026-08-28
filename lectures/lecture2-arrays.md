# CS50 Lecture 2 · 数组 & 命令行参数 · 2026.08.03

## 1. 命令行参数：argc 和 argv

### 是什么

运行程序的时候，除了 `./程序名`，还能在后面带参数：

```
./caesar 3
```

`3` 就是参数。C 语言用 `main` 的括号来接收它：

```c
int main(int argc, string argv[])
```

### argc = 参数个数

```
./caesar 3 → argc = 2
./caesar → argc = 1
./caesar 3 hello → argc = 3
```

规律：**argc = 空格分隔的词的数量**。程序名本身算一个。

### argv = 参数数组

```
argv[0] = "./caesar" ← 永远是程序名
argv[1] = "3" ← 第一个参数
argv[2] = "hello" ← 第二个参数
```

注意：**argv[1] 是字符串，不是数字！** `"3"` ≠ `3`

### 验证参数数量

```c
if (argc != 2)
{
 printf("Usage: ./caesar key\n");
 return 1; // 1 表示出错了
}
```

## 2. 字符串转数字：atoi()

`argv[1]` 是字符串 `"3"`，不能直接做加减。用 `atoi()` 转换：

```c
#include <stdlib.h> // atoi 在这里

int key = atoi(argv[1]); // "3" → 3
```

`atoi` = **A**SCII **to** **I**nteger

## 3. ASCII 码

计算机里所有字符本质都是数字：

```
'A' = 65 'B' = 66 ... 'Z' = 90
'a' = 97 'b' = 98 ... 'z' = 122
'0' = 48 '1' = 49 ... '9' = 57
```

### 字符可以当数字用

```c
char c = 'A';
int n = c; // n = 65

char d = 66; // d = 'B'

char e = 'C' + 1; // e = 'D'
```

跟昨天学的 `isalpha()` 不一样，这里直接做加减法。

## 4. 凯撒加密公式

### 核心思想

把 A-Z 这 26 个字母看成一个环。Z 后面回到 A。

```
A B C ... X Y Z A B C ...
0 1 2 23 24 25
```

### 步骤

1. 把字母变成 0-25：`s[i] - 'A'`
2. 加上密钥：`+ key`
3. 取余 % 26，超了绕回来
4. 加回 'A'

```
大写：cipher = (s[i] - 'A' + key) % 26 + 'A'
小写：cipher = (s[i] - 'a' + key) % 26 + 'a'
```

### 例子：H + 3

```
'H' = 72
'H' - 'A' = 72 - 65 = 7
7 + 3 = 10
10 % 26 = 10
10 + 'A' = 65 + 10 = 75 = 'K'
```

H → K，对了。

### 例子：Z + 1

```
'Z' - 'A' = 25
25 + 1 = 26
26 % 26 = 0
0 + 'A' = 'A'
```

Z → A，绕回来了。

### 非字母不管

```c
if (isupper(s[i])) // 大写
{
 s[i] = (s[i] - 'A' + key) % 26 + 'A';
}
else if (islower(s[i])) // 小写
{
 s[i] = (s[i] - 'a' + key) % 26 + 'a';
}
// 其他的（空格、标点、数字）原样保留
```

### 新函数：isupper() 和 islower()

```c
isupper('A') → true isupper('a') → false
islower('a') → true islower('A') → false
```

都在 `<ctype.h>` 里，跟 `isalpha()` 一个家。

## 5. 完整流程

```
./caesar 3
 ↓
检查 argc == 2？ ← 不是就报错
 ↓
atoi(argv[1]) 得到 key ← 把 "3" 变成 3
 ↓
get_string 读入明文 ← 昨天学的
 ↓
遍历每个字符：
 - 大写 → 公式加密
 - 小写 → 公式加密
 - 其他 → 原样
 ↓
打印密文
```

## 常见报错

| 报错 | 原因 | 修复 |
|------|------|------|
| `segmentation fault` | 没检查 argc 就用了 argv[1] | 先 `if (argc != 2)` |
| `incompatible integer` | 把 "3" 直接当数字用了 | 用 `atoi()` |
| `implicit declaration of atoi` | 没 include stdlib.h | `#include <stdlib.h>` |
| 输出乱码 | 忘了 `% 26`，值超出字母范围 | 加上取余 |
