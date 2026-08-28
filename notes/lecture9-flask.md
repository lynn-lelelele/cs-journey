# CS50 L9 · Flask 后端入门(第一性原理版)

> 日期：2026-08-28　｜　进度：L9 进行中（约 40%）　｜　成果：3 页 Flask 网站 + 亲手加路由

---

## 0. 第一性原理：一切从"两台电脑想说话"开始

### 网络 = 电脑之间的"邮政系统"
- 每台电脑可以开很多"窗口"（端口）等着收信
- Flask 程序开在 **5000 端口**，浏览器是发信人，Flask 是收信+回信人

### 一次通信 = 请求 → 响应（后端的全部本质）
```
浏览器输入网址 → 发信(要 /skills)
 → Flask 收信，查登记本(@app.route)
 → 执行对应函数 → return 回信内容
 → 浏览器显示
```

### 静态 vs 动态
- 静态：双击 index.html，浏览器直接读文件（死的）
- 动态：Flask 程序现场算出来返回（活的，能根据数据变化）

### Flask 是什么（一句话）
**Flask = 帮你处理"收信、查登记本、回信"的 Python 库。你只负责在登记本上写：网址 → 函数 → 返回啥。**

---

## 1. 代码全解（对照请求→响应循环）

```python
from flask import Flask, render_template      # 拿工具
app = Flask(__name__)                          # 开窗口，准备当服务器

@app.route("/")                                # 登记本第1行
def home():                                    # 处理 / 的函数
    return '<h1>这是主页</h1><a href="/about">关于我</a> <a href="/skills">技能</a>'

@app.route("/about")                           # 登记本第2行
def about():
    return render_template("about.html")       # 回信：读模板文件发回

@app.route("/skills")                          # 登记本第3行
def skills():
    return render_template("skills.html")

if __name__ == "__main__":                     # 直接运行本文件时
    app.run()                                  # 开 5000 窗口，开始收信
```

| 代码 | 角色 |
|---|---|
| `app = Flask(__name__)` | 开窗口，准备当服务器 |
| `@app.route("/xxx")` | 在登记本写"网址 → 函数" |
| `def xxx():` | 处理这个网址的函数 |
| `return ...` | 回信内容 |
| `app.run()` | 开始收信（一直等） |

---

## 2. 模板 render_template

### 书写逻辑（= 函数调用）
```
return  render_template(  "about.html"  )
  │            │               │
  │            │               └ 参数：模板文件名（Flask 自动去 templates 文件夹找）
  │            └ 调用函数：读文件变成页面
  └ 把结果交回给 Flask → 发给浏览器
```

- 和你会的 `str(121)` 一样：函数名 + 括号 + 参数
- 模板放 **templates 文件夹**，只写文件名不写路径
- 为什么不用 return 字符串？字符串是死的，模板是活的（能塞变量）

### 模板文件结构（HTML + 变量占位）
```html
<!-- templates/about.html -->
<h1>关于我</h1>
<p>我是 Lynn...</p>
<a href="/">← 回主页</a>
```

---

## 3. 自己加一个路由（完整流程）

```python
@app.route("/test")
def test():
    return "测试成功"
```
1. 加在 app.py（if __name__ 上面）
2. `Ctrl+S` 保存
3. 重启服务器（`Ctrl+C` → `python app.py`）
4. 访问 `/test` → 看到"测试成功"

---

## 4. 踩坑记录（今天连踩三次！）

1. **改代码后页面没变 → 99% 是没重启服务器**。Flask 非 debug 模式缓存旧模板/代码
   - 解决：`Ctrl+C` 停 → `python app.py` 重启
   - 或者用 `app.run(debug=True)`，改完自动重载
2. **复制文件 ≠ 内容自动变**：复制 about.html 成 skills.html，内容还是"关于我"，要自己改 + 保存
3. **旧服务器进程顽固**：多次"重启"可能没杀掉真正占端口的进程 → 按进程号杀（Get-NetTCPConnection 查端口 owner → Stop-Process -Id）
4. **VSCode 没打开文件夹**：只打开单个文件时，左侧资源管理器看不到 templates → 用 `code 桌面路径` 打开文件夹

---

## 5. 下一步
- [ ] L9 剩余：Finance 项目（表单、session、数据库）
- [ ] FastAPI 教程前 4 章（学完 Flask 再碰，快一倍）
- [ ] W1 力扣：Two Sum 哈希版 ✅ 完成
