import random

class ACC:
    def __init__(self, username, password, question, pinluns):
        self.username = username
        self.password = password
        self.question = question
        self.pinlun = random.choice(pinluns) if isinstance(pinluns, list) else pinluns

# 多账号配置
accounts = {
    "用户名": ACC(
        username="用户名",
        password="密码",
        question="答案",
        pinluns=[
            "感谢分享！！！！！",
            "谢谢楼主~",
            "冲冲冲！",
            "来了来了！",
            "感谢分享！！",
        ],
    ),

}
