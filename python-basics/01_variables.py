"""
第 01 章：变量与数据类型

本章讲什么：
    变量怎么赋值、Python 的动态类型、命名规则；int / float / str / bool / None 五个基本类型；
    list / tuple / dict / set 四个容器长什么样；类型转换、字符串基础，以及可变与不可变。

学完能做什么：
    把一份零散的成绩数据存进变量和容器，做类型转换、求平均、去重、排序，
    并避开 input 返回字符串、浮点误差、除号与整除这几个常见坑。

怎么跑：
    python 01_variables.py
"""

# 1. 变量赋值与动态类型
# 变量名 = 值，赋值时不用声明类型。
# 同一个变量可以先后装不同类型的数据，这叫动态类型。
score = 92
print(score)            # 输出：92
print(type(score))      # 输出：<class 'int'>

score = 92.5            # 同一个名字换成浮点数，完全合法
print(score)            # 输出：92.5
print(type(score))      # 输出：<class 'float'>

# 2. 同时赋值与交换
# 等号两边都用逗号，可以一次给多个变量赋值。
x, y = 88, 92
print(x, y)             # 输出：88 92

x, y = y, x             # 一行完成交换，不需要临时变量
print(x, y)             # 输出：92 88

first, *rest = [88, 92, 79]    # 带星号收集剩下的元素
print(first, rest)             # 输出：88 [92, 79]

# 3. 变量命名规则与 snake_case
# 规则：只能用字母、数字、下划线；不能以数字开头；不能是关键字；区分大小写。
# 风格：多个单词用小写加下划线连接，也就是 snake_case。
class_avg = 87.5        # 推荐写法：班级平均分
total_score_2 = 300     # 可以有数字，但别放开头
# 下面两行是错的，取消注释会报 SyntaxError：
# 2nd_score = 88        # 不能以数字开头
# class = "一班"        # class 是 Python 关键字

import keyword
print(keyword.iskeyword("class"))        # 输出：True
print(keyword.iskeyword("class_avg"))    # 输出：False

# 4. 五个基本类型
count = 5                  # int      整数
avg = 87.5                 # float    浮点数
course = "统计学"           # str      字符串
passed = True              # bool     布尔值，只有 True / False
result = None              # NoneType 空值，表示"还没有结果"

print(count, avg, course, passed, result)    # 输出：5 87.5 统计学 True None
print(type(count), type(avg))
# 输出：<class 'int'> <class 'float'>
print(type(course), type(passed), type(result))
# 输出：<class 'str'> <class 'bool'> <class 'NoneType'>

# 5. type() 与 isinstance()
# type() 给出精确类型；isinstance() 判断"是不是这类（含子类）"，更常用。
print(type(avg) is float)                  # 输出：True
print(isinstance(avg, float))              # 输出：True
print(isinstance(count, (int, float)))     # 输出：True，一次判断多种类型
print(isinstance(True, int))               # 输出：True，bool 是 int 的子类

# 6. 类型转换
# 常见四件套：int() float() str() bool()。能转就转，转不了会直接报错。
print(int("95"))        # 输出：95     字符串数字转整数
print(int(95.8))        # 输出：95     小数转整数是截断，不是四舍五入
print(float("95.5"))    # 输出：95.5
print(str(95) + "分")    # 输出：95分   转成字符串才能拼接
print(bool(0), bool(""), bool([]), bool(-1))
# 输出：False False False True    0、空串、空列表为假，其余为真

try:
    int("九十五")          # 不是数字字符串，转不了
except ValueError as e:
    print("报错：", e)
# 输出：报错： invalid literal for int() with base 10: '九十五'

# 7. 字符串基础
# 单引号和双引号等价；字符串里要出现引号时，换另一种包住就行。
name = "小明"
quote = '他说："分数够了"'
print(quote)                                   # 输出：他说："分数够了"

# f-string：字符串前加 f，用 {} 直接嵌入变量或表达式
score = 92.5
print(f"{name}的成绩是{score}分")                # 输出：小明的成绩是92.5分
print(f"平均分 {sum([88, 92, 79]) / 3:.1f}")     # 输出：平均分 86.3

# 转义字符：\n 换行，\t 制表符，\\ 表示反斜杠本身
print(repr("姓名\t分数"))                       # 输出：'姓名\t分数'
print(len("小明\n好"))                          # 输出：4     \n 只算一个字符

# 三引号可以写多行字符串，换行被原样保留
report = """成绩单
姓名：小明
分数：92.5"""
print(report.splitlines()[0])                  # 输出：成绩单
print(report.count("\n"))                      # 输出：2

# 8. 四个容器认脸（深入用法留到后面的章节）
scores = [88, 92, 79]                  # list  列表：有序、可修改，用中括号
point = (88, 92)                       # tuple 元组：有序、不可修改，用小括号
stats = {"小明": 92, "小红": 88}         # dict  字典：键到值的映射，用花括号
names = {"小明", "小红", "小明"}          # set   集合：自动去重、无序，用花括号

print(scores[0], scores[-1])           # 输出：88 79     按下标取，-1 是最后一个
print(point[1])                        # 输出：92
print(stats["小明"])                    # 输出：92        按 key 取值
print(len(names), sorted(names))       # 输出：2 ['小明', '小红']    重复项已去掉

# 9. 可变与不可变
# str 不可变：+= 会生成一个新字符串，id 随之改变。
word = "小"
before = id(word)
word += "明"
print(word, id(word) == before)        # 输出：小明 False

# list 可变：+= 在原列表上就地修改，id 不变。
nums = [1, 2]
before = id(nums)
nums += [3]
print(nums, id(nums) == before)        # 输出：[1, 2, 3] True

# 别名问题：b = a 只是让两个名字指向同一个列表，不是复制。
a = [88, 92]
b = a
b.append(79)
print(a)                               # 输出：[88, 92, 79]   a 被一起改了
print(a is b)                          # 输出：True

# 想要独立副本，用 .copy()
c = a.copy()
c.append(60)
print(a)                               # 输出：[88, 92, 79]
print(c)                               # 输出：[88, 92, 79, 60]

# 10. 常见坑 1：input() 返回的永远是字符串
# 错的写法：
# score = input("请输入分数：")    # 用户输入 88，拿到的却是 "88"
# print(score + 1)                # TypeError：字符串不能和数字相加

raw = "88"                        # 假装这是 input() 的返回值
try:
    raw + 1
except TypeError as e:
    print("报错：", e)
# 输出：报错： can only concatenate str (not "int") to str

# 正确写法：先用 int() 转成数字，再做运算
score = int(raw)
print(score + 1)                  # 输出：89

# 11. 常见坑 2：浮点误差，0.1 + 0.2 不等于 0.3
print(0.1 + 0.2)                  # 输出：0.30000000000000004
print(0.1 + 0.2 == 0.3)           # 输出：False

# 正确写法一：判断"足够接近"，用 math.isclose
import math
print(math.isclose(0.1 + 0.2, 0.3))    # 输出：True

# 正确写法二：比较前先四舍五入
print(round(0.1 + 0.2, 2) == 0.3)      # 输出：True

# 12. 常见坑 3：/ 得到浮点数，// 才是整除
print(7 / 2)                      # 输出：3.5     / 永远返回 float
print(7 // 2)                     # 输出：3       向下取整
print(-7 // 2)                    # 输出：-4      注意是向下，不是向零截断
print(7 % 2)                      # 输出：1       取余，常用来判断奇偶

# 统计场景：算平均分用 /
scores = [88, 92, 79]
print(sum(scores) / len(scores))  # 输出：86.33333333333333
print(sum(scores) // len(scores)) # 输出：86

# 自测题：把每题下面的"参考答案"取消注释后运行，对照输出。
# 1. 把字符串 "88" 转成整数，再转成浮点数，并打印两者的类型。
# 参考答案：
# n = int("88")
# print(n, type(n), float(n), type(float(n)))
# 输出：88 <class 'int'> 88.0 <class 'float'>

# 2. 交换 a、b 两个变量的值，要求不借助第三个变量。
# 参考答案：
# a, b = 1, 2
# a, b = b, a
# print(a, b)
# 输出：2 1

# 3. 用 f-string 输出"总分 259，平均 86.3"（平均分保留一位小数）。
# 参考答案：
# scores = [88, 92, 79]
# print(f"总分 {sum(scores)}，平均 {sum(scores) / len(scores):.1f}")
# 输出：总分 259，平均 86.3

# 4. 用 isinstance 判断 87.5 是不是浮点数。
# 参考答案：
# print(isinstance(87.5, float))
# 输出：True

# 5. 把 ["小明", "小红", "小明"] 去重后按名字排序输出。
# 参考答案：
# names = ["小明", "小红", "小明"]
# print(sorted(set(names)))
# 输出：['小明', '小红']

# 6. 用一个变量存分数列表，再让另一个变量指向它并 append，验证原列表也变了。
# 参考答案：
# scores = [88, 92, 79]
# ref = scores
# ref.append(60)
# print(scores)
# 输出：[88, 92, 79, 60]

# 7. 正确比较 0.1 + 0.2 与 0.3，不许用 ==。
# 参考答案：
# import math
# print(math.isclose(0.1 + 0.2, 0.3))
# 输出：True

# 8. 求 4 个分数的平均值（要 float）和它的整数部分（用 //）。
# 参考答案：
# scores = [88, 92, 79, 60]
# print(sum(scores) / len(scores), sum(scores) // len(scores))
# 输出：79.75 79
