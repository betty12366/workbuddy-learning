# 学习 Python 语法中的注释
print("Hello, World!")

# 这是一个注释，用于解释代码的功能
# 注释不会被 Python 解释器执行，只是用来说明代码的作用
# 注释可以放在代码的上方、下方或旁边，帮助其他人理解代码的逻辑

# Python 中的变量
# 变量是用于存储数据的命名空间。在 Python 中，变量不需要声明类型

print("Hello, World!")
metric = 0.032
type(metric)
a = 1

a1 = 0.032
print(type(a1))

a2 = 100
print(type(a2))

# 运算符
## 算术运算符
x = 10
y = 3
print(x + y, x - y, x * y, x / y, x // y, x % y, x ** y)

## 赋值运算符
x = 5
print(x)
x += 2
print(x)

## 比较运算符
print(x == y, x != y, x > y, x < y, x >= y, x <= y)

## 逻辑运算符
print(x > 0 and y > 0, x > 0 or y < 0, not (x > 0))

## 成员运算符
a4 = [1, 2, 3, 4, 5]
a5 = [6, 7, 8, 9, 10]
print(2 in a4, 5 not in a5)

import 模块A
print(模块A.变量A)

print("打招呼（小明）")

from zai import ZhipuAiClient
client = ZhipuAiClient(api_key="YOUR_API_KEY")
response = client.chat.completions.create(
    model="glm-5.3",
    messages=[
        {"role": "system", "content": "您是一个有用的AI助手。"},
        {"role": "user", "content": "您好，请介绍一下自己。"}
    ],
    temperature=0.6
)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"我的名字是{self.name}，今年{self.age}岁。")

    def say_hello(self):
        print(f"你好，我是{self.name}。")

小强 = Person("小强", 10)
小强.introduce()
小强.say_hello()