# -*- coding: utf-8 -*-
"""
CS Journey 自我检查脚本
用法：
    python check_update.py           # 只检查，输出报告
    python check_update.py --update  # 检查 + 自动 commit/push（有改动时）
"""
import os
import subprocess
import sys
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))


def run(cmd):
    """在仓库目录执行命令，返回输出文本"""
    try:
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
        return r.stdout.strip()
    except Exception as e:
        return f"[error] {e}"


def main():
    print("=" * 52)
    print(f"  CS Journey 自我检查  ·  {date.today()}")
    print("=" * 52)

    # 1. 未提交的改动
    status = run(["git", "status", "--short"])
    if status:
        print("\n[!] 有未提交的改动：")
        print(status)
    else:
        print("\n[OK] Git 工作区干净")

    # 2. 未推送的 commit
    unpushed = run(["git", "log", "origin/master..HEAD", "--oneline"])
    if unpushed:
        print("\n[!] 有未推送的 commit：")
        print(unpushed)
    else:
        print("[OK] 全部已推送")

    # 3. 笔记清单
    notes_dir = os.path.join(ROOT, "notes")
    notes = sorted(os.listdir(notes_dir)) if os.path.isdir(notes_dir) else []
    print(f"\n-- 笔记（{len(notes)} 份）--")
    for n in notes:
        if n.endswith((".md", ".py")):
            print("  ", n)

    # 4. 学习项目清单
    print("\n-- 学习项目 --")
    for item in sorted(os.listdir(ROOT)):
        full = os.path.join(ROOT, item)
        if os.path.isdir(full) and item.startswith("20"):
            for d in sorted(os.listdir(full)):
                if os.path.isdir(os.path.join(full, d)):
                    print(f"   {item}/{d}")

    # 5. 桌面未归档的学习文件提醒
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    if os.path.isdir(desktop):
        loose = sorted(f for f in os.listdir(desktop)
                       if f.endswith((".py", ".c")) and not f.startswith("~"))
        if loose:
            print(f"\n[!] 桌面有 {len(loose)} 个未归档的学习文件（考虑放进仓库）：")
            for f in loose:
                print("    -", f)
        else:
            print("\n[OK] 桌面无散落学习文件")

    # 6. --update：自动提交推送
    if "--update" in sys.argv:
        changed = status or unpushed
        if not changed:
            print("\n[OK] 没有需要更新的内容")
            return
        run(["git", "add", "-A"])
        run(["git", "commit", "-m", f"auto-update {date.today()}"])
        push_out = run(["git", "push"])
        if "master -> master" in push_out or "main -> main" in push_out:
            print("\n[OK] 已自动 commit + push")
        else:
            print("\n[?] push 输出：")
            print(push_out)
    print("\n" + "=" * 52)


if __name__ == "__main__":
    main()
