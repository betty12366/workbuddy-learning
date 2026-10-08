"""
第 4 章：流程控制（if / while / for）

本章讲什么：
  1. if / elif / else，以及“缩进就是语法”
  2. 真值判断：哪些值算 False
  3. while、break / continue、while-else
  4. for：range 三种用法 / 遍历 list、str、dict / enumerate / zip
  5. 循环嵌套
  6. 两个经典陷阱：边遍历边改列表、死循环
  7. 常见坑：for-else、elif 与多个 if、range(len(x))
  8. 可选：match / case 结构模式匹配（Python 3.10+）

学完能做什么：按分数区间打等级、算及格率、找最大值、统计各分数段人数、跳过缺考数据、累加求和。

怎么跑（VS Code 终端里一行命令）：python 04_flow_control.py
"""

# 1. if / elif / else：缩进就是语法
# 条件成立就执行对应代码块，从上往下只命中第一个成立的分支。
# Python 不用大括号，靠缩进划分代码块，官方建议每层 4 个空格。
score = 87
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"
print(grade)
# 输出：B
# Tab 和空格看起来一样，但 Python 3 不允许同一个文件里混用，混用会报
# TabError: inconsistent use of tabs and spaces in indentation。
# 稳妥做法：VS Code 设 "editor.insertSpaces": true、"tabSize": 4，
# 统一按 Tab 键，让编辑器自己插入 4 个空格。
if score >= 60:
    level = "及格"                    # 缩进 4 空格，属于 if 内部
print("判断结束，等级 =", level)       # 回到顶格，不属于 if
# 输出：判断结束，等级 = 及格

# 2. 真值判断：哪些值算 False
# 任何对象都能当条件。下面这些“空、零、无”的值算 False：
#   0 / 0.0（0j 同理）    ""       []  ()      {}      set()
#   None                  False
# 其余（非零数字、非空容器、非空字符串）都算 True，
# 所以判断“有没有数据”写 if data: 就等于写 if len(data) > 0:。
values = [0, 0.0, "", [], {}, set(), None, False, 3, "0", [0]]
print([v for v in values if not v])
print(bool(3), bool("0"), bool([0]))
# 输出：
# [0, 0.0, '', [], {}, set(), None, False]
# True True True

# 3. while、break / continue、while-else
# while 条件成立就重复执行；计数型循环必须自己让条件变假，这里靠 i += 1。
total = 0
i = 1
while i <= 5:          # 累加 1..5
    total += i
    i += 1
print(total)
# 输出：15
# break 立刻跳出整个循环；continue 跳过本次剩余语句，直接进下一轮。下面 -1 表示缺考，不处理。
valid = []
for s in [88, -1, 59, 100, 0, 73]:
    if s < 0:
        continue
    if s == 100:
        break
    valid.append(s)
print(valid)
# 输出：[88, 59]
# while-else：循环“正常结束”（条件变假）才执行 else，被 break 打断则不执行。
n = 1
while n <= 3:
    n += 1
else:
    print("正常结束，n =", n)         # 条件变假 -> else 执行
# 输出：正常结束，n = 4
n = 1
while True:
    if n == 3:
        break
    n += 1
else:
    print("这行不会打印")             # 被 break 打断 -> else 整段跳过
print("break 退出，n =", n)
# 输出：break 退出，n = 3

# 4. for 循环：range / 遍历容器 / enumerate / zip
# range 三种用法：range(stop) / range(start, stop) / range(start, stop, step)
print(list(range(5)))              # 0 到 4
print(list(range(2, 6)))           # 2 到 5
print(list(range(0, 10, 3)))       # 0, 3, 6, 9
# 输出：
# [0, 1, 2, 3, 4]
# [2, 3, 4, 5]
# [0, 3, 6, 9]
# 遍历列表直接拿元素；遍历字符串拿到一个个字符（中文也按字符算）。
for g in ["A", "B", "C"]:
    print(g)
for ch in "统计":
    print(ch)
# 输出：
# A
# B
# C
# 统
# 计
# 遍历字典：默认给 key，要值用 values()，要键值对用 items()。
counts = {"优秀": 2, "及格": 5, "不及格": 1}
for k in counts:
    print(k, counts[k])
print(list(counts.values()))
for k, v in counts.items():
    print(k, "=", v)
# 输出：
# 优秀 2
# 及格 5
# 不及格 1
# [2, 5, 1]
# 优秀 = 2
# 及格 = 5
# 不及格 = 1
# enumerate() 顺带给下标，start 可指定起点；zip() 并行遍历，长度不同以短的为准。
names, scores = ["张三", "李四", "王五"], [88, 76, 95]
for idx, name in enumerate(names, start=1):
    print(idx, name)
for name, s in zip(names, scores):
    print(name, s)
# 输出：
# 1 张三
# 2 李四
# 3 王五
# 张三 88
# 李四 76
# 王五 95

# 5. 循环嵌套：统计各分数段人数
# 外层遍历分数段，内层扫一遍全部分数并计数，共 4 * 8 = 32 次比较。
scores = [55, 72, 88, 91, 63, 47, 100, 79]
bands = [("不及格", 0, 59), ("及格", 60, 79), ("良好", 80, 89), ("优秀", 90, 100)]
for label, low, high in bands:
    count = 0
    for s in scores:
        if low <= s <= high:
            count += 1
    print(label, count)
# 输出：
# 不及格 2
# 及格 3
# 良好 1
# 优秀 2

# 6. 两个经典陷阱
# 陷阱 1：边遍历边删除会漏元素——删掉一个后后面整体前移，下标却继续往前走。
dirty = [55, -1, -1, 72, 88]
for s in dirty:
    if s < 0:
        dirty.remove(s)
print(dirty)
# 输出：[55, -1, 72, 88]      <- 还剩一个 -1，漏删了
dirty = [55, -1, -1, 72, 88]
print([s for s in dirty if s >= 0])   # 正确做法：推导式筛出来；想原地删就遍历副本 dirty[:]
# 输出：[55, 72, 88]
# 陷阱 2：忘了改变循环条件，条件永远成立 -> 死循环。下面这段千万别真跑：
#   i = 1
#   while i <= 5:
#       print(i)        # 忘了写 i += 1，i 永远是 1
# 防呆：写完 while 先问“哪个变量会让条件变假？它被改了吗？”
# 计数型循环优先用 for + range，天然不会忘记自增。

# 7. 常见坑
# 坑 1：for-else 不是“if 的否则”，而是“循环没被 break 过才执行 else”。
for s in [55, 72, 88, 91]:
    if s == 95:
        print("找到了", s)
        break
else:
    print("所有分数里都没有 95")
# 输出：所有分数里都没有 95
# 坑 2：elif 只会命中一个分支；写成多个独立 if 会各自判断，可能覆盖结果。
score = 95
if score >= 90:
    g1 = "优秀"
elif score >= 60:
    g1 = "及格"
else:
    g1 = "不及格"
if score >= 90:
    g2 = "优秀"
if score >= 60:
    g2 = "及格"        # 第二个 if 也成立，把“优秀”覆盖成了“及格”
print(g1, g2)
# 输出：优秀 及格
# 坑 3：只要元素就别用 range(len(x)) 绕圈，需要下标时用 enumerate。
nums = [55, 72, 88]
for i in range(len(nums)):       # 能用，但绕了一圈
    print(nums[i])
for i, n in enumerate(nums):     # 需要下标就用它
    print(i, n)
# 输出：
# 55
# 72
# 88
# 0 55
# 1 72
# 2 88

# 8. 可选：match / case 结构模式匹配（仅 Python 3.10+）
# 注意：match / case 是 3.10 才有的语法。在 3.9 及更低版本运行本节，
# 整个文件会直接 SyntaxError（连启动都启动不了），请升级 Python 或用下面的 if 写法。
def grade_of(score):
    match score:
        case s if s >= 90:       # 带守卫（if）的捕获模式
            return "优秀"
        case s if s >= 60:
            return "及格"
        case _:                  # _ 表示兜底
            return "不及格"

def grade_of_if(score):          # 等价的 if 写法，3.8 也能跑
    if score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

print(grade_of(95), grade_of(70), grade_of(40), grade_of_if(95))
# 输出：优秀 及格 不及格 优秀

# 9. 自测题
# 先自己想，再取消下面“答案”里的注释对照运行。
# 题 1：score = 87，用 if / elif / else 打出 A / B / C / D 等级。期望：B
# 题 2：scores = [55, 72, 88, 91, 63]，算及格率（>=60 的占比），打印成百分数。期望：60.0%
# 题 3：同上的 scores，找出最大值（不许用 max）。期望：91
# 题 4：用 for + range 求 1 + 2 + ... + 100。期望：5050
# 题 5：scores = [88, -1, 59, 100]，用 continue 跳过 -1，再求和。期望：247
# 题 6：判断 0、"0"、None、[]、[0] 里哪些算 False。期望：0、None、[] 为 False
# 题 7：nums = [3, 1, 4, 1, 5]，用 for-else 判断 9 在不在里面。期望：9 不在列表里
# 题 8：stats = {"优秀": 3, "及格": 5}，用 items() 打印 “优秀=3” 这种形式。
# 答案（取消注释即可运行）：
# print("A" if 87 >= 90 else "B" if 87 >= 80 else "C" if 87 >= 60 else "D")
# sc = [55, 72, 88, 91, 63]
# print(str(round(sum(1 for x in sc if x >= 60) / len(sc) * 100, 1)) + "%")
# mx = sc[0]
# for x in sc: mx = x if x > mx else mx
# print(mx)
# print(sum(range(1, 101)))
# print(sum(x for x in [88, -1, 59, 100] if x >= 0))
# print([v for v in [0, "0", None, [], [0]] if not v])
# for n in [3, 1, 4, 1, 5]:
#     if n == 9:
#         print("9 在列表里")
#         break
# else:
#     print("9 不在列表里")
# print([k + "=" + str(v) for k, v in {"优秀": 3, "及格": 5}.items()])
