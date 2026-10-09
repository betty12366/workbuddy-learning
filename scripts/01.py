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

from zhipuai import ZhipuAI
client = ZhipuAI(api_key="api-key")
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

# 变量类型
a1 = 10
a2 = 2.2
a3 = "Hello"
a4 = [1, 2, 3]
a5 = (4, 5, 6)
a6 = {"key1": "value1", "key2": "value2"}
a7 = {1, 2, 3}
a8 = None
a9 = True

print(type(a1), type(a2), type(a3), type(a4), type(a5), type(a6), type(a7), type(a8), type(a9))  # <class 'int'>
## 字符串的格式化
name = "小明"
age = 10
print(f"我的名字是{name}，今年{age}岁。")

## 流程控制

## 条件语句

x = 10
y = 20

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

## 循环语句

for i in range(5):
    print(i)


while x > 0:
    print(x)
    x -= 1
    ## 函数

def 打招呼(姓名, 内容="你好"):
    print(f"{内容}, {姓名}!")
    return f"{内容}, {姓名}!"
打招呼("小明")

# 模块与包

import 模块A

print(模块A.变量A)
print(模块A.函数A())

from 模块A import 变量B

print(变量B)

result = 打招呼("小红", "早上好")
print(result)

# 异常处理

try:
    result = 10 / 0

except ZeroDivisionError:
    print("除以零错误！")

    import os
from dotenv import load_dotenv
from zhipuai import ZhipuAI

load_dotenv()  # 读取当前目录 .env

api_key = os.environ.get("ZHIPU_API_KEY")
if not api_key:
    raise RuntimeError("未找到 ZHIPU_API_KEY，请检查 .env 文件")

# 初始化客户端
client = ZhipuAI(api_key=api_key)

# 创建聊天完成请求
response = client.chat.completions.create(
    model="glm-4-flash",
    messages=[
        {"role": "system", "content": "您是一个有用的AI助手。"},
        {"role": "user", "content": "您好，请介绍一下自己。"},
    ],
    temperature=0.6,
)

# 获取回复
print(response.choices[0].message.content)

def zhipuAI(提示词, temperature=0.6):


    import os
    from dotenv import load_dotenv
    from zai import ZhipuAiClient

    load_dotenv()  # 读取当前目录 .env

    api_key = os.environ.get("ZHIPU_API_KEY")
    if not api_key:
        raise RuntimeError("未找到 ZHIPU_API_KEY，请检查 .env 文件")

    # 初始化客户端
    client = ZhipuAiClient(api_key=api_key)

    # 创建聊天完成请求
    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=[
            {"role": "system", "content": "您是一个有用的AI助手。"},
            {"role": "user", "content": f"{提示词}"},
        ],
        temperature=temperature,
    )

        # 获取回复
    return response.choices[0].message.content

zhipuAI("您好，请介绍一下西北民族大学广告学专业。") 

