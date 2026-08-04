# CS50 Lecture 3 补充 · struct 与 typedef · 2026.08.04

## struct = 把东西打包成"档案袋"

以前一个变量只能装一个东西，struct 可以把多个东西打包：

```c
struct
{
    string name;   // 袋子里有：名字
    int votes;     // 袋子里还有：票数
};
```

## typedef = 给类型起名字

```c
typedef struct
{
    string name;
    int votes;
}
candidate;   // 起名 candidate，以后像 int/string 一样用
```

## 怎么用

```c
candidate c;        // 创建袋子 c
c.name = "lynn";    // 点 . 访问字段
c.votes = 0;

printf("%s 有 %d 票\n", c.name, c.votes);
```

## 数组 + struct（Plurality 场景）

```c
candidate candidates[3];      // 3 个候选人的袋子数组
candidates[0].name = "lynn";
candidates[1].name = "mario";
```

## 一句话总结

- struct = 打包（定义袋子里装啥）
- typedef = 起名（用 candidate 代替一长串）
- 点 . = 打开袋子拿东西（c.name）

## 容易混的点

- struct 只定义类型，不创建变量
- 定义完记得末尾分号 `};`
- 访问用 `.` 不是 `->`（`->` 是指针用的，后面学到）
