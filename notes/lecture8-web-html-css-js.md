# CS50 L8 · Web 入门(HTML + CSS + JavaScript)

> 日期：2026-08-27　｜　成果：第一个个人主页（含白天/黑夜模式按钮）

---

## 0. 三兄弟分工（最重要的框架）

| 语言 | 负责 | 类比 |
|---|---|---|
| HTML | 骨架：这是什么 | 毛坯房结构 |
| CSS | 化妆：长什么样 | 装修 |
| JavaScript | 动作：会响应点击 | 电灯开关 |

---

## 1. HTML 基础

### 开标签 / 闭标签 / 内容

```
<h1>  你好,我是 Lin  </h1>
开标签    内容      闭标签
```

- 开标签 `<名字>`，闭标签 `</名字>`（名字前多一个 `/`，表示"到这里结束"）
- 闭标签不能省：否则浏览器不知道标记到哪结束
- 类比：就像引号 `"内容"`，有始有终

### 基本骨架

```html
<!DOCTYPE html>
<html>
  <head>
    <title>我的第一个网页</title>
  </head>
  <body>
    <h1>一级标题</h1>
    <p>段落</p>
    <a href="https://github.com/lynn-lelelele">链接</a>
  </body>
</html>
```

- `<head>` = 后台信息区（title 显示在标签页上，用户看不到）
- `<body>` = 用户看到的所有内容
- `<h1>`~`<h6>` 标题逐级变小，`<p>` 段落，`<a>` 链接

### 属性（attribute）= 标签的"设置项"

```
<标签名  属性名="值"> 内容 </标签名>
```

- `<a href="网址">` → href 是属性，告诉链接去哪
- `<img src="图片.jpg">` → src 是图片来源
- 类比 C：`printf("hello")` 里 `"hello"` 是函数的参数；属性就是标签的参数

---

## 2. CSS 基础

### 写法一：内联样式（给单个标签化妆）

```html
<h1 style="color: blue; font-size: 40px; text-align: center;">标题</h1>
```

格式：`属性: 值;`，多个用分号隔开

### 写法二：`<style>` 标签 + 选择器（规范写法，一次管一类）

```html
<style>
  h1  { color: blue; }
  p   { font-size: 25px; }
  body { background-color: #00fff2; }
  a   { color: #a3e4b0; }
</style>
```

- 选择器（`h1`/`p`/`body`/`a`）= 选中哪些标签
- 花括号里 = 怎么化妆
- **十六进制颜色**：`#RRGGBB`（红/绿/蓝各两位），`#00fff2` 是青色

### 常用属性速查

| 属性 | 作用 |
|---|---|
| `color` | 文字颜色 |
| `font-size` | 字号 |
| `background-color` | 背景色 |
| `text-align` | 对齐（center 居中） |

---

## 3. JavaScript 基础（让网页动起来）

### 第一个交互：按钮点击改背景色

```html
<button onclick="document.body.style.backgroundColor = 'yellow'">点我变黄</button>
```

拆解：
- `onclick="..."` = 点击时执行引号里的代码
- `document` = 当前网页
- `document.body` = 网页的"身体"
- `document.body.style.backgroundColor = 'yellow'` = 把背景色赋值为黄色（和 C 的 `x = 5` 一样是赋值）

### 多个动作用分号隔开

```html
<button onclick="document.body.style.backgroundColor='black'; document.body.style.color='white'">黑夜模式</button>
```

### JS 和 CSS 的关系
- CSS 定默认样式，JS 可以"覆盖"它（点了按钮，JS 临时改样式）

---

## 4. 今日成品（Lynn 写的第一个主页）

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      h1 { color: blue; }
      p  { font-size: 25px; }
      body { background-color: #00fff2 }
      a { color: #a3e4b0; }
    </style>
  </head>
  <body>
    <h1>lynn</h1>
    <p>欢迎来到我的个人主页！</p>
    <button onclick="document.body.style.backgroundColor = 'yellow'">点我变黄</button>
    <button onclick="document.body.style.backgroundColor='white'; document.body.style.color='black'">白天模式</button>
    <button onclick="document.body.style.backgroundColor='black'; document.body.style.color='white'">黑夜模式</button>
    <a href="https://github.com/lynn-lelelele">我的 GitHub</a>
  </body>
</html>
```

---

## 5. 踩坑记录

1. **改样式不是加新行，是改原来的行**——新手常加一行空的 `<h1 style="..."></h1>`，结果看不到（没字）。要直接改有内容的那行
2. **样式规则末尾加分号**——最后一条不加也能跑，但加了好习惯
3. **删错内容按 `Ctrl + Z` 撤销**，可以连按多次
4. **找不到文件**——固定保存位置（如桌面），VSCode 里 `Ctrl+O` 打开

---

## 6. 下一步

- [ ] L8 继续：JavaScript 进阶（function、if/else）+ 完成 Homepage 完整版
- [ ] L9 Flask（Python 做后端）
- [ ] 上传到 GitHub Pages 让别人能访问


---

## 7. JS 进阶：function + if/else（一个按钮来回切换）

### 升级思路
- 内联一堆代码 → 太乱
- 打包成函数 → 起个名字，按钮一行调用

### 代码（Lynn 亲手写的切换按钮）

```html
<button onclick="toggle()">点我变黑/白</button>

<script>
  function toggle() {
    if (document.body.style.backgroundColor == 'black') {
      document.body.style.backgroundColor = 'white';
      document.body.style.color = 'black';
    } else {
      document.body.style.backgroundColor = 'black';
      document.body.style.color = 'white';
    }
  }
</script>
```

### 语法要点
- `<script>` = JS 代码的家（放 `<body>` 末尾）
- `function 名字() { ... }` = 定义函数（和 C 的 `void 名字(void)` 一个概念）
- `onclick="toggle()"` = 点击时调用函数，括号 `()` 表示"执行它"
- `if (条件) { ... } else { ... }` = 判断，和 C 完全一样
- `==` 是"等于"（比较），`=` 是赋值，别混

### 逻辑
点一下 → 看当前背景是不是黑色 → 是则切白天，否则切黑夜 → 来回切换

### 与 C 的对照（Lin 的已有知识）
| C | JS |
|---|---|
| `void toggle(void)` | `function toggle()` |
| `if (x == 5) {...} else {...}` | 一样 |
| 函数调用 `toggle();` | `toggle()` |
