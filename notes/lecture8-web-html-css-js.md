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


---

## 8. Homepage 升级：列表 + 图片 + class 选择器 + 排查思维

### 列表 <ul> / <li>
```html
<h2>我的技能</h2>
<ul>
  <li>C 语言</li>
  <li>Python / pandas</li>
  <li>机器学习</li>
</ul>
```
- `<ul>` = 无序列表（unordered list）
- `<li>` = 列表项（list item）

### 图片 <img> 与两种路径
```html
<img src="https://github.com/lynn-lelelele.png" width="150">  <!-- 网络地址：需要网络 -->
<img src="avatar.png" width="150">                            <!-- 相对路径：找网页旁边的文件 -->
```
- `src` = 图片来源，`width` = 宽度
- **相对路径** `avatar.png`：浏览器去 index.html 所在文件夹找，不用网络，秒开

### class 选择器（给指定的元素化妆）
```html
<h2 class="title">我的技能</h2>   <!-- ① 贴便签 -->
```
```css
.title { color: purple; }          <!-- ② 按便签找 -->
```
- `h2 { }` 选所有 h2；`.title { }` 只选贴了 class="title" 的
- 点号 `.` = "我要找贴了这个便签的"
- 便签可以贴多个元素，也可以摘掉（摘掉样式就没了）

### 排查思维（重要！）
代码"看起来对但不工作"时，先分清两类问题：
| 类型 | 例子 | 检查方式 |
|---|---|---|
| ① 代码本身错 | 语法错、标签错 | 看报错 / 对照规则 |
| ② 环境/资源问题 | 网络不通、文件不存在 | 检查资源能不能访问 |

> 实例：GitHub 头像显示不出来 = 代码没错，是网络要梯子。换成本地文件就好。

### 今日完整成品
（见桌面 index.html：青色背景 + 技能列表 + 本地头像 + 变黄按钮 + 白天/黑夜切换 + 紫色标题）


---

## 9. Homepage 多页面骨架 + 界面美化

### 页面跳转(相对路径)
```html
<nav>
  <a href="index.html">主页</a>
  <a href="skills.html">技能</a>
  <a href="projects.html">项目</a>
  <a href="contact.html">联系我</a>
</nav>
```
- 4 个页面放同一文件夹,`href="skills.html"` 相对路径互相跳
- `<nav>` = 导航区语义标签;当前页用 `class="active"` 高亮

### hover 悬停效果
```css
a:hover { color: red; }
button:hover { background-color: lightblue; }
```
- `:hover` = 鼠标停上去时的状态,一行 CSS 就让元素"有反应"

### 界面美化三件套(所有"高级感"的来源)
```css
.card   { border: 1px solid #e5e7eb; border-radius: 10px; padding: 20px; }
button  { border: 1px solid #e5e7eb; border-radius: 8px; padding: 8px 20px; }
.avatar { border-radius: 50%; }
```
1. **border**:细浅灰边框 → 元素从背景"浮"出来
2. **border-radius**:圆角 → 越圆越柔和;`50%` 变正圆(头像)
3. **padding**:内边距/留白 → 越透气越高级

### 页面风格设计(8-27 定稿：克制展示)
- 不喊口号,用数字说话(首页一排统计:`3` Kaggle / `0.97082` AUC / `3` LeetCode / `L1-L7` CS50)
- 克制配色:白底 + 浅灰 + 一个蓝主色
- 不用 emoji

### 主题切换按钮(JS)
```html
<button onclick="document.body.style.backgroundColor = '#111827'; document.body.style.color = '#e5e7eb'">深色</button>
```
- 一行 JS 直接改 body 背景色/文字色
- 多个动作用分号隔开

### 今日 Homepage 文件(桌面)
- index.html / skills.html / projects.html / contact.html(4 页互通)
- 风格:简约高级,白底 + 蓝主色
- 待办:填内容、加交互、传 GitHub Pages


---

## 10. 🏁 L8 收工：Homepage 达标检查单（2026-08-27）

| CS50 要求 | 实现 |
|---|---|
| ≥4 个页面 | index / skills / projects / contact |
| 每页 ≥1 链接 | 导航栏（`<nav>` + `<a href>`） |
| 每页 ≥1 列表 | 技能 / 工具 / 进行中 / 状态（`<ul><li>`） |
| 每页 ≥3 种 CSS 属性 | 白底 + 主色 + 卡片 |
| ≥1 页有图片 | index 头像（`border-radius: 50%` 圆形） |
| ≥1 页有按钮 + JS | 主题切换按钮（onclick 改背景色） |

**L8 完成！** 下一站：L9 Flask（Python 后端）。
