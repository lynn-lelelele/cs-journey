# CS50 L9 · Flask 后端入门(第一性原理版)

> 适用读者：有 Python 基础、刚接触 Web 后端的初学者。
> 学习目标：理解 HTTP 请求-响应模型，掌握 Flask 路由、视图函数与模板渲染。

---

## 1. 底层模型：HTTP 请求与响应

Web 后端的一切都建立在 **HTTP 协议**的请求-响应循环之上。

### 参与者

| 角色 | 专业术语 | 比喻 |
|---|---|---|
| 浏览器 | 客户端（Client） | 顾客 / 发信人 |
| Flask 程序 | 服务器（Server） | 服务员 / 收信人 |
| 5000 端口 | 监听端口（Port） | 收信窗口 |

### 一次完整通信

```
客户端请求：GET /skills
    ↓
服务器收到请求，查路由表
    ↓
执行对应的视图函数 → 生成响应内容
    ↓
服务器返回响应（HTTP Response）
    ↓
浏览器渲染显示
```

> 类比：网络如同邮政系统。每个程序在指定端口"监听"来信；浏览器发出请求，服务器处理并返回响应。

### 静态 vs 动态

- **静态页面**：浏览器直接读取磁盘上的 HTML 文件，内容固定。
- **动态页面**：服务器端程序**实时生成**内容（可结合数据库、用户状态等），每次请求的结果可以不同。

---

## 2. Flask 的核心：路由与视图函数

Flask 是一个 WSGI 应用框架，负责处理网络通信的底层细节。开发者只需声明 **路由（Route）** 与对应的 **视图函数（View Function）**。

```python
from flask import Flask, render_template

app = Flask(__name__)                    # 创建 Flask 应用实例

@app.route("/")                          # 路由装饰器：绑定 URL 路径与函数
def home():                              # 视图函数
    return '<h1>这是主页</h1><a href="/about">关于我</a>'

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()                            # 启动开发服务器，开始监听
```

### 逐部分说明

| 代码 | 作用 |
|---|---|
| `app = Flask(__name__)` | 实例化 Flask 应用，准备处理请求 |
| `@app.route("/xxx")` | **路由装饰器**：将 URL 路径映射到函数 |
| `def xxx():` | 视图函数：处理该路径请求的逻辑 |
| `return ...` | 生成响应内容（字符串或模板） |
| `app.run()` | 启动开发服务器，监听默认端口 5000 |

> 比喻：路由表如同餐厅的"点单本"，每个 URL 路径对应一道菜（视图函数）的做法。

---

## 3. 模板渲染：render_template

### 为什么需要模板

视图函数返回的可以是纯字符串，但复杂页面需要大量 HTML。**模板（Template）**将 HTML 从 Python 代码中分离，便于维护与复用。

```
return  render_template(  "about.html"  )
    │           │              │
    │           │              └─ 模板文件名（Flask 自动在 templates/ 目录查找）
    │           └─ 调用模板引擎渲染
    └─ 将渲染结果作为响应返回
```

- 模板文件统一放在 **`templates/`** 目录下，代码中只需写文件名。
- 模板支持变量占位与逻辑控制（Jinja2 语法），后续可传入数据动态渲染。

```html
<!-- templates/about.html -->
<h1>关于我</h1>
<p>我是 XXX...</p>
<a href="/">← 返回主页</a>
```

---

## 4. 开发服务器与调试模式

```python
if __name__ == "__main__":
    app.run(debug=True)    # 开启调试模式
```

- **开发服务器**：`app.run()` 启动的本地服务器，仅用于开发调试，**不可用于生产环境**。
- **调试模式**（`debug=True`）：代码修改后自动重载，并显示详细错误页。开发期推荐开启。

---

## 5. 常见问题

1. **修改代码后页面无变化**：服务器仍在运行旧版本。需重启服务器（`Ctrl+C` 停止后重新运行 `python app.py`），或开启调试模式自动重载。
2. **复制模板文件但内容未变**：文件内容不会随文件名改变，需手动修改并保存。
3. **端口被占用**：旧服务器进程未完全退出。可通过 `Get-NetTCPConnection -LocalPort 5000` 查询占用进程，并强制结束。
4. **资源管理器看不到 templates 目录**：VSCode 需以文件夹方式打开项目（`code <项目路径>`），而非单个文件。

---

## 6. 术语表

| 术语 | 含义 |
|---|---|
| 客户端 / 服务器 | 发起请求的一方 / 处理请求并响应的一方 |
| HTTP 请求 / 响应 | 浏览器发出的请求报文 / 服务器返回的响应报文 |
| 端口 | 操作系统分配给网络服务的编号 |
| 路由（Route） | URL 路径与处理函数的映射关系 |
| 视图函数 | 处理特定路径请求的函数 |
| 装饰器（Decorator） | Python 语法，用于扩展函数行为 |
| 模板渲染 | 用模板引擎将模板文件渲染为 HTML |
| 开发服务器 | 本地开发用的简易服务器 |

---

## 7. 下一步

- [ ] CS50 L9 完成：Finance 项目（表单、Session、数据库）
- [ ] FastAPI 教程前 4 章（掌握 Flask 后学习更高效）


---

## 8. 表单(Form):让用户提交数据

### HTML 表单

```html
<form action="/login" method="post">
  <input type="text" name="name" placeholder="你的名字">
  <button type="submit">提交</button>
</form>
```

| 代码 | 功能 |
|---|---|
| `<form>` | 表单容器,圈住输入与按钮 |
| `action="/login"` | 提交后数据发往的地址 |
| `method="post"` | 发送方式:POST(提交数据) |
| `input type="text"` | 文本框(用户输入) |
| `name="name"` | 字段名,服务器据此取值 |
| `placeholder` | 输入框内的灰色提示文字 |
| `button type="submit"` | 提交按钮 |

### GET 与 POST(记忆:GET = 拿,POST = 交)

- GET:浏览器**拿**页面/数据(只读,如访问网页)。
- POST:浏览器**交**数据(提交表单,数据放在请求体中)。

### 接收数据

```python
@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")   # 从表单数据中取字段
    return f"你好, {name}!"
```

- `request` :本次请求对象(浏览器发来的一切)。
- `request.form` :表单数据(类似字典)。
- `.get("name")` :取出 name 字段的值。

---

## 9. Session(登录状态)[重点难点]

> HTTP 是无状态的:服务器默认**不记得**上一次请求是谁。Session 用于在多次请求间记住用户身份。

### 机制(一式两份)

```
登录 → 服务器存档案 {编号: 用户名} + 浏览器存 cookie(编号)
访问 → 浏览器自动带 cookie → 服务器查档案 → 认出用户
```

- **服务器**:session 数据 + session_id。
- **浏览器**:cookie(仅保存 session_id)。

### 代码

```python
from flask import Flask, session
app.secret_key = "任意密钥"          # cookie 加密密钥(必需)

@app.route("/login", methods=["POST"])
def login():
    session["username"] = request.form.get("name")  # 写卡
    return "登录成功!"

@app.route("/profile")
def profile():
    name = session.get("username")   # 读卡
    if name:
        return f"欢迎回来, {name}!"
    return "你还没登录"
```

### 为什么换浏览器就"失忆"

- cookie(卡片)存在**浏览器软件**里,不在人/电脑上。
- 换浏览器 / 清缓存 / 换电脑 → 卡片丢失 → 服务器查不到档案。

> 类比:健身会员卡放在钱包里;换钱包(浏览器) = 卡没带 = 前台不认识。

### 关键点

| 操作 | 语法 | 含义 |
|---|---|---|
| 写 | `session["key"] = 值` | 记住 |
| 读 | `session.get("key")` | 想起来 |
| 依赖 | `app.secret_key` | cookie 加密,不设会报错 |
