"""第 2 章 运算符

本章讲什么：
    算术、比较、逻辑、成员、身份、位运算这六类运算符，
    它们的优先级、复合赋值写法，以及 Python 特有的短路求值规则。

学完能做什么：
    独立写出成绩是否及格、分数区间判断、及格率统计、数据筛选条件这类表达式，
    并且知道 == 和 is 什么时候会坑人、浮点数为什么不能直接用 == 比较。

怎么跑：
    python 02_operators.py
"""

import math

# 1. 算术运算符
# + - * / 是加减乘除，注意 / 的结果永远是 float，能整除也是 float。
# // 是向下取整（floor），不是向零截断，负数上会和 C、Java 不一样。
# % 是取余，** 是幂（2 ** 10 就是 2 的 10 次方）。
scores = [87, 93, 78, 90, 66]
print("总分 =", scores[0] + scores[1] + scores[2] + scores[3] + scores[4])  # 输出：总分 = 414
print("平均分 =", 414 / 5)          # 输出：平均分 = 82.8
print("整除 =", 7 // 2)             # 输出：整除 = 3
print("负整除 =", -7 // 2)          # 输出：负整除 = -4
print("取余 =", 7 % 2)              # 输出：取余 = 1
print("幂 =", 2 ** 10)              # 输出：幂 = 1024
print("开平方 =", 16 ** 0.5)        # 输出：开平方 = 4.0

# 取余常用来判断奇偶、轮流分组（第几题该发给第几个人）。
print("77 是偶数吗 =", 77 % 2 == 0)  # 输出：77 是偶数吗 = False

# 2. 运算符优先级
# 从高到低：**  →  一元 +x / -x  →  * / // %  →  + -  →  比较  →  not  →  and  →  or
# 两个容易记错的点：** 从右往左结合；** 的优先级高于一元负号。
# 记不住就加括号，括号最省钱，也最好读。
print("先乘后加 =", 2 + 3 * 4)      # 输出：先乘后加 = 14
print("加括号 =", (2 + 3) * 4)      # 输出：加括号 = 20
print("幂右结合 =", 2 ** 3 ** 2)    # 输出：幂右结合 = 512
print("负号与幂 =", -2 ** 2)        # 输出：负号与幂 = -4
print("括号改负号 =", (-2) ** 2)    # 输出：括号改负号 = 4

# 3. 复合赋值 += -= *= /= //= **=
# x op= y 等价于 x = x op y，只是写法更短，少写一遍变量名。
# 累加分数是最典型的用法。
acc = 0
acc += 90        # 等价于 acc = acc + 90
acc += 85
acc -= 5
print("累加分 =", acc)              # 输出：累加分 = 170

avg = 90
avg /= 3                           # 除法赋值，结果变成 float
print("avg =", avg)                # 输出：avg = 30.0

groups = 37
groups //= 5
print("groups =", groups)          # 输出：groups = 7

n = 2
n **= 3
print("n =", n)                    # 输出：n = 8

r = 10
r %= 3
print("r =", r)                    # 输出：r = 1

# 字符串也能 +=（拼接），列表能 +=（追加多个元素）。
label = "及格率"
label += "："
label += "80%"
print(label)                       # 输出：及格率：80%

# 4. 比较运算符与链式比较
# == != > < >= <= 算出来的一律是 bool：True 或 False。
# 链式比较 0 <= x <= 100 等价于 0 <= x and x <= 100，但中间的操作数只算一次。
score = 78
print("是否及格 =", score >= 60)      # 输出：是否及格 = True
print("是否满分 =", score == 100)      # 输出：是否满分 = False
print("不是满分 =", score != 100)      # 输出：不是满分 = True

x = 85
print("0 <= x <= 100 =", 0 <= x <= 100)  # 输出：0 <= x <= 100 = True
print("区间外 =", 0 <= 120 <= 100)        # 输出：区间外 = False

# 布尔值参与比较时，True 当 1、False 当 0。
print("True == 1 =", True == 1)          # 输出：True == 1 = True
print("False == 0 =", False == 0)        # 输出：False == 0 = True

# 5. 逻辑运算符 and / or / not 与短路求值
# and：两边都真才真；or：有一个真就真；not：取反。
# 短路求值：and 左边为假时右边不执行，or 左边为真时右边不执行。
print("and =", 78 >= 60 and 78 < 90)   # 输出：and = True
print("or =", 45 >= 60 or 78 >= 60)    # 输出：or = True
print("not =", not (78 >= 60))         # 输出：not = False

# 用有副作用的函数演示短路：每次调用都往 calls 里记一笔。
calls = []


def record(name, value):
    calls.append(name)
    return value


result = record("A", False) and record("B", True)
print("and 结果 =", result, "调用过 =", calls)          # 输出：and 结果 = False 调用过 = ['A']

calls.clear()
result = record("A", True) or record("B", False)
print("or 结果 =", result, "调用过 =", calls)           # 输出：or 结果 = True 调用过 = ['A']

calls.clear()
result = record("A", False) or record("B", 0)
print("两边都执行 =", result, "调用过 =", calls)         # 输出：两边都执行 = 0 调用过 = ['A', 'B']

# 实战用法：先判断列表非空再取首元素，用 and 短路避免 IndexError。
empty = []
print("空列表短路 =", empty and empty[0] >= 60)         # 输出：空列表短路 = []

# 6. 成员运算符 in / not in
# in 判断"在不在里面"：列表看元素，字符串看子串，字典只看 key。
scores = [88, 92, 75, 60, 45]
print("60 在列表里 =", 60 in scores)        # 输出：60 在列表里 = True
print("100 在列表里 =", 100 in scores)      # 输出：100 在列表里 = False
print("59 不在列表里 =", 59 not in scores)  # 输出：59 不在列表里 = True

topic = "统计学基础"
print("含 统计 =", "统计" in topic)          # 输出：含 统计 = True

# 字典的 in 只看 key，不看 value，这点最容易踩。
student = {"name": "小明", "score": 88}
print("name 在字典里 =", "name" in student)             # 输出：name 在字典里 = True
print("小明 在字典里 =", "小明" in student)              # 输出：小明 在字典里 = False
print("小明 在值里 =", "小明" in student.values())       # 输出：小明 在值里 = True

# 7. 身份运算符 is / is not 与 == 的区别
# == 比"值是否相等"，is 比"是不是同一个对象"（同一块内存）。
a = [88, 92]
b = [88, 92]
print("== 比内容 =", a == b)      # 输出：== 比内容 = True
print("is 比身份 =", a is b)      # 输出：is 比身份 = False
c = a
print("别名同对象 =", a is c)     # 输出：别名同对象 = True

# 判 None 一律用 is / is not，这是 Python 的惯例。
missing = None
print("是 None =", missing is None)          # 输出：是 None = True
print("不是 None =", missing is not None)    # 输出：不是 None = False

# 小整数缓存：-5 到 256 的整数在 CPython 里全局复用同一个对象。
small_a = int("256")
small_b = int("256")
print("256 同一对象 =", small_a is small_b)  # 输出：256 同一对象 = True
big_a = int("1000")
big_b = int("1000")
print("1000 同一对象 =", big_a is big_b)     # 输出：1000 同一对象 = False
# 缓存只是实现细节，比数值永远用 ==，用 is 会写出时灵时不灵的 bug。

# 8. 常见坑一：把 == 写成 is
# 错的写法：用 is 比较学号
id_a = int("1000")
id_b = int("1000")
print("用 is 的结果 =", id_a is id_b)     # 输出：用 is 的结果 = False
# 为什么错：is 比的是对象身份。id_a 和 id_b 是两个不同的 int 对象，
# 只是值恰好相等；换成 256 以内的小数字又会碰巧判成 True，
# 于是这个 bug 时灵时不灵，最难查。
# 正确写法：数值、字符串、容器一律用 ==，只有和 None 比身份时才用 is。
print("用 == 的结果 =", id_a == id_b)     # 输出：用 == 的结果 = True

# 9. 常见坑二：浮点数不能用 == 直接比
# 错的写法：加权总分理论上就是 72.9，直接比
weights = [0.3, 0.3, 0.4]
scores = [88, 59, 72]
weighted = 0
for w, s in zip(weights, scores):
    weighted += w * s                # 循环累加，统计里最常见的写法
print("weighted =", weighted)                # 输出：weighted = 72.89999999999999
print("weighted == 72.9 =", weighted == 72.9)  # 输出：weighted == 72.9 = False
# 为什么错：0.3、0.1 这类十进制小数在二进制浮点里存不下，
# 每一步都带一点点误差，累加之后误差被放大。
# 正确写法：用 math.isclose，或者用差值阈值。
print("isclose =", math.isclose(weighted, 72.9))          # 输出：isclose = True
print("差值阈值 =", abs(weighted - 72.9) < 1e-9)          # 输出：差值阈值 = True
# 单个数同理：0.7 + 0.1 并不等于 0.8。
print("0.7 + 0.1 =", 0.7 + 0.1)                          # 输出：0.7 + 0.1 = 0.7999999999999999

# 10. 常见坑三：and / or 返回的是操作数本身，不是 True / False
# 错的写法：以为 or 一定返回 bool
nick = 0 or "缺考"
print("nick =", nick, type(nick).__name__)   # 输出：nick = 缺考 str
# 为什么错：and / or 返回"决定结果的那个操作数"，不做类型转换。
# 0 是假值，所以 or 把右边的字符串原样返回了。
print("bool 化后 =", bool(0 or "缺考"))          # 输出：bool 化后 = True
print("都假返回后一个 =", repr(0 or ""))         # 输出：都假返回后一个 = ''
# 这个特性用来设默认值很方便，但别当布尔值用：统计里 0 分和"没成绩"是两回事。
raw_score = 0
wrong_score = raw_score or 60     # 错：0 分被当成没填，直接被改成了 60 分
print("错误的默认值 =", wrong_score)             # 输出：错误的默认值 = 60
# 正确写法：要区分 0 和 None，就显式判断。
score = raw_score if raw_score is not None else 60
print("显式判断 =", score)                       # 输出：显式判断 = 0

# 11. 常见坑四：% 对负数取模的结果和 C / Java 不同
# 错的写法：以为 -7 % 2 是 -1
print("-7 % 2 =", -7 % 2)          # 输出：-7 % 2 = 1
print("7 % -2 =", 7 % -2)          # 输出：7 % -2 = -1
# 为什么错：Python 的 // 是向下取整、% 的符号跟着除数走，
# 并且永远满足 (a // b) * b + a % b == a。
print("恒等式 =", (-7 // 2) * 2 + (-7 % 2))   # 输出：恒等式 = -7
# 想要 C / Java 那种"余数跟着被除数"的效果，用 math.fmod。
print("fmod =", math.fmod(-7, 2))             # 输出：fmod = -1.0
# 统计场景：对标准化后的 z 分数（可能为负）做分箱时，
# 用 % 分组要留意方向，否则负数会被分到上一个箱子里。

# 自测题（共 8 题）
# 每题下面都有一段注释掉的参考答案，先自己写，再取消注释对照输出。
# 约定：scores 是某次考试的全班成绩。
scores = [88, 59, 72, 45, 95, 61, 80, 39, 100, 55]

# 题 1：用链式比较判断 score = 88 是否落在 [60, 100] 内。
score = 88
# print("1)", 60 <= score <= 100)
# 输出：1) True

# 题 2：求及格率（>= 60 算及格），用 round 保留 2 位小数。
# print("2)", round(sum(1 for s in scores if s >= 60) / len(scores) * 100, 2))
# 输出：2) 60.0

# 题 3：用复合赋值循环累加全班总分。
# total = 0
# for s in scores:
#     total += s
# print("3)", total)
# 输出：3) 694

# 题 4：判断 88 是偶数（% 和 & 都试试）。
# print("4)", 88 % 2 == 0, 88 & 1 == 0)
# 输出：4) True True

# 题 5：判断字典里有没有"数学"这门课，以及有没有"语文"这门课。
# exam = {"数学": 88, "英语": 92}
# print("5)", "数学" in exam, "语文" in exam)
# 输出：5) True False

# 题 6：两个内容相同的列表，分别用 == 和 is 比较。
# a = [88, 92]
# b = [88, 92]
# print("6)", a == b, a is b)
# 输出：6) True False

# 题 7：用 math.isclose 判断 0.1 + 0.2 是否等于 0.3。
# print("7)", 0.1 + 0.2 == 0.3, math.isclose(0.1 + 0.2, 0.3))
# 输出：7) False True

# 题 8：写出 -2 ** 2 和 (-2) ** 2 的值，体会 ** 与一元负号的优先级。
# print("8)", -2 ** 2, (-2) ** 2)
# 输出：8) -4 4
