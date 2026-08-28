# CS50 Lecture 8 · Web 前端基础(HTML + CSS + JavaScript) · 课堂笔记

> 适用读者：零前端基础的初学者。
> 学习目标：理解网页的三种核心技术——HTML 结构、CSS 样式、JavaScript 交互，并完成一个多页面个人站点。

---

## 0. 三兄弟的分工

| 技术 | 职责 | 类比 |
|---|---|---|
| HTML | 结构：定义页面元素 | 毛坯房结构 |
| CSS | 样式：控制元素外观 | 装修 |
| JavaScript | 行为：响应用户交互 | 电灯开关 |

---

## 1. HTML：页面结构

### 元素(Element)与标签(Tag)

```html
<h1>你好，我是 XXX</h1>
```

- **开标签** `<名字>` 与**闭标签** `</名字>` 成对出现，中间为内容。
- 闭标签不能省略，否则浏览器无法确定元素边界。
- 类比：类似引号 `"内容"`，有始有终。

### 文档基本结构

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

- `<head>`：元数据区（`<title>` 显示在浏览器标签页，用户不可见页面内容）。
- `<body>`：页面主体，用户可见内容。
- 常见语义标签：`<h1>`~`<h6>` 标题、`<p>` 段落、`<a>` 链接、`<img>` 图片、`<ul>/<li>` 列表、`<nav>` 导航。

### 属性(Attribute)

```html
<标签名 属性名="值"> 内容 </标签名>
```

- `href`：链接地址；`src`：图片来源；`width`：宽度；`class`：样式类名。
- 类比：属性类似函数参数（如 `printf("hello")` 中的 `"hello"`）。

---

## 2. CSS：样式与选择器

### 内联样式

```html
<h1 style="color: blue; font-size: 40px; text-align: center;">标题</h1>
```

格式：`属性: 值;`，多条用分号分隔。

### 选择器(Selector)

```css
h1 { color: blue; }        /* 标签选择器：所有 h1 */
.title { color: purple; }  /* 类选择器：class="title" 的元素 */
a:hover { color: red; }    /* 伪类：鼠标悬停时 */
```

- 类选择器用 `.类名` 匹配 `class` 属性。
- `:hover` 为伪类，表示元素的悬停状态。

### 常用样式属性

| 属性 | 作用 |
|---|---|
| `color` | 文字颜色 |
| `font-size` | 字号 |
| `background-color` | 背景色 |
| `text-align` | 对齐方式 |
| `border` / `border-radius` | 边框 / 圆角 |
| `padding` / `margin` | 内边距 / 外边距（留白） |

> 界面美感三要素：细边框 + 圆角 + 留白。

---

## 3. JavaScript：交互

### 事件处理(onclick)

```html
<button onclick="document.body.style.backgroundColor = 'yellow'">点我变黄</button>
```

- `onclick`：点击事件。
- `document`：DOM 文档对象；`document.body.style` 可动态修改样式。

### 函数与条件分支

```html
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
<button onclick="toggle()">切换主题</button>
```

- `function 名字()`：定义函数；`onclick="toggle()"` 调用函数。
- `if/else` 语法与 C 一致。

---

## 4. 多页面与相对路径

```html
<nav>
  <a href="index.html">主页</a>
  <a href="skills.html">技能</a>
</nav>
```

- 同一目录下，用文件名即可跳转（相对路径）。
- 图片同理：`src="avatar.png"` 表示网页同目录下的本地文件。

---

## 术语表

| 术语 | 含义 |
|---|---|
| 元素 / 标签 | HTML 的组成单元 |
| 属性 | 元素的配置参数 |
| 选择器 | CSS 匹配元素的方式 |
| 类(class) | 给元素分组以便统一设置样式 |
| 伪类 | 元素的特定状态（如 hover） |
| 事件 | 用户操作触发的信号（如点击） |
| DOM | 浏览器将 HTML 表示为可操作的对象树 |
| 相对路径 | 相对于当前文件的路径 |

## 学习进度

- [x] HTML 结构 / 属性
- [x] CSS 选择器 / 样式
- [x] JavaScript 交互
- [x] 多页面个人站点(Homepage)
