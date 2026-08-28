# C 语言常用头文件速查表 · 课堂笔记

> 适用读者：初学 C 语言者。
> 头文件(Header File)：函数与宏的声明集合。`#include` 将其引入当前源文件，从而使用其中声明的函数。

## 速查表

| 头文件 | 里面有什么 | 记忆法 |
|--------|-----------|--------|
| `stdio.h` | printf / scanf / fgets | standard input output 输入输出 |
| `cs50.h` | get_string / get_int / get_float | CS50 专用 |
| `string.h` | strlen / strcmp / strcpy / strcat | 字符串 |
| `ctype.h` | isalpha / isdigit / islower / toupper | char type 字符判断 |
| `stdlib.h` | atoi / malloc / free | standard library 通用工具 |
| `math.h` | round / sqrt / pow | 数学 |
| `stdbool.h` | bool / true / false | 布尔类型 |

## 逐个详解

### stdio.h — 输入输出 [重要度:高]
```c
printf("你好%d\n", n); // 打印
scanf("%d", &n); // 读整数
```

### cs50.h — CS50 专用 [重要度:高]
```c
string s = get_string("名字: ");
int n = get_int("数字: ");
```

### string.h — 字符串 [重要度:高]
```c
strlen(s); // 长度
strcmp(a, b); // 比较，==0 表示一样
strcpy(dst, src); // 复制
strcat(dst, src); // 拼接
```

### ctype.h — 字符判断 [重要度:中]
```c
isalpha(c); // 字母？
isdigit(c); // 数字？
islower(c); // 小写？
isupper(c); // 大写？
toupper(c); // 转大写
tolower(c); // 转小写
```

### stdlib.h — 通用工具 [重要度:中]
```c
atoi("123"); // 字符串 → 整数
malloc(n); // 申请内存
free(p); // 释放内存
```

### math.h — 数学 [重点]
```c
round(2.6); // 四舍五入 → 3
sqrt(16); // 开根号 → 4
pow(2, 3); // 2³ → 8
```

### stdbool.h — 布尔
```c
bool ok = true;
```

## 两个坑

1. math.h 编译要加 `-lm`：`gcc test.c -o test -lm`
2. 用了函数忘 include 对应头文件 → 编译器报"undeclared"

## 记法

- 先想：我用了哪个函数？→ 就要哪个头文件
- stdio = 输入输出，stdlib = 通用工具，ctype = 字符判断
