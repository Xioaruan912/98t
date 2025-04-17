from flask import Flask, render_template_string, request
from threading import Thread
from datetime import datetime
import random
import time
from config import accounts
from login import input_main

# 初始化 Flask 应用
app = Flask(__name__)

# 记录每次运行的结果
execution_logs = []

def run_task_once_per_day():
    while True:
        for acc in accounts.values():
            # 随机等待 0 到 24 小时内的一个时间
            delay_seconds = random.randint(0, 24 * 3600)
            time.sleep(delay_seconds)

            try:
                status = input_main(acc)
            except Exception as e:
                status = f"失败: {e}"

            execution_logs.append({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "username": acc.username,
                "status": status
            })

# HTML 模板，包含选择框和手动签到按钮
html = """
<!DOCTYPE html>
<html>
<head>
    <title>98签到</title>
    <style>
        body { font-family: "Microsoft YaHei", Arial, sans-serif; padding: 20px; color: #333; }
        h1 { color: #007bff; font-size: 24px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); }
        th, td { border: 1px solid #ddd; padding: 12px; text-align: center; }
        th { background-color: #f8f9fa; font-weight: bold; }
        tr:nth-child(even) { background-color: #f4f4f4; }
        tr:hover { background-color: #f1f1f1; }
        .success { color: #28a745; }
        .failed { color: #dc3545; }
        select, button { margin-top: 20px; padding: 8px; }
    </style>
</head>
<body>
    <h1>98签到历史</h1>
    <form method="POST" action="/">
        <label for="selected_account">选择账号：</label>
        <select id="selected_account" name="selected_account">
            {% for account in accounts %}
            <option value="{{ account }}">{{ account }}</option>
            {% endfor %}
        </select>
        <button type="submit">手动签到</button>
    </form>
    <p>{{ message }}</p>
    <table>
        <tr>
            <th>执行时间</th>
            <th>账号</th>
            <th>执行结果</th>
        </tr>
        {% for log in logs %}
        <tr>
            <td>{{ log.timestamp }}</td>
            <td>{{ log.username }}</td>
            <td class="{{ 'success' if log.status == '成功' else 'failed' }}">{{ log.status }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        selected_username = request.form.get("selected_account")
        acc = accounts.get(selected_username)
        if acc:
            try:
                status = input_main(acc)
                execution_logs.append({
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "username": acc.username,
                    "status": status
                })
                message = f"手动签到成功：{acc.username}"
            except Exception as e:
                message = f"手动签到失败：{e}"
        else:
            message = "未找到该账号！"

    return render_template_string(html, logs=execution_logs, accounts=accounts.keys(), message=message)

if __name__ == "__main__":
    # 启动任务线程
    task_thread = Thread(target=run_task_once_per_day, daemon=True)
    task_thread.start()

    app.run(host="0.0.0.0", port=5000)
