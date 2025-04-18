import random

class ACC:
    def __init__(self, username, password, question, pinluns):
        self.username = username
        self.password = password
        self.question = question
        self.pinlun = random.choice(pinluns) if isinstance(pinluns, list) else pinluns

# 多账号配置
accounts = {


}
