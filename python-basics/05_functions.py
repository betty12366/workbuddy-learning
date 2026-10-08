"""
05 函数：把重复的数据处理代码包起来。

本章讲什么：
    def 定义 / docstring / 调用 / return（不写 return 就返回 None）；
    位置参数、关键字参数、默认参数；*args 与 **kwargs；位置-only 与关键字-only（/ 和 *，3.8+）；
    作用域与 LEGB、global / nonlocal 的用法和代价；可变默认参数这个大坑；
    函数是一等对象、常用内置函数、类型注解（注解不会被强制检查）。
学完能做什么：
    把重复的统计代码抽成函数，写出带默认参数的 mean / median / 方差函数，
    用 sorted(key=...) 按分数排序，避开"可变默认参数"和"函数里改全局变量"两大高频错误。
怎么跑：
    python 05_functions.py
"""

# 1. 定义、docstring、调用、return
# def 函数名(参数): 后面缩进四格的是函数体；函数体首行的字符串是 docstring，用 __doc__ 能读到。
# return 把结果交回调用处并立刻结束函数；没写 return 的函数不是"没返回值"，而是返回 None。
def mean(scores):
    """返回一组分数的平均值；空列表返回 0.0。"""
    if not scores:                 # 先挡住空列表，否则下面除以 0
        return 0.0
    return sum(scores) / len(scores)

print(mean([80, 90, 100]))         # 输出：90.0
print(mean([]))                    # 输出：0.0
print(mean.__doc__)                # 输出：返回一组分数的平均值；空列表返回 0.0。

def log_score(score):
    """只打印，不返回任何东西。"""
    print(f"记录分数: {score}")

result = log_score(88)             # 输出：记录分数: 88
print(result)                      # 输出：None

# 2. 位置参数、关键字参数、默认参数
# 位置参数按顺序传；关键字参数写 名字=值，顺序可以换；默认参数有默认值，调用时可省略。
# 默认值在函数"定义时"求值一次（第 6 节看它的坑）。位置参数必须写在关键字参数前面。
def summarize(scores, digits=2, label="平均分"):
    """按 label 汇总分数，保留 digits 位小数。"""
    return f"{label}: {round(mean(scores), digits)}"

print(summarize([1, 2, 4]))                                 # 输出：平均分: 2.33
print(summarize([1, 2, 4], 0))                              # 输出：平均分: 2.0
print(summarize([1, 2, 4], label="中位分"))                  # 输出：中位分: 2.33
print(summarize(scores=[1, 2, 4], digits=1, label="均值"))    # 输出：均值: 2.3

# 3. *args 与 **kwargs
# *args 把多出来的位置参数打包成元组；**kwargs 把关键字参数打包成字典（args / kwargs 只是习惯名）。
# 调用时反过来，* 和 ** 能把列表 / 字典拆开再传进去。
def all_mean(*groups):
    """对每一组分数分别求平均，返回保留 1 位小数的列表。"""
    return [round(mean(g), 1) for g in groups]

def describe(**info):
    """把关键字参数整理成 "键=值" 的列表。"""
    return [f"{k}={v}" for k, v in info.items()]

print(all_mean([80, 90], [60, 70, 80]))      # 输出：[85.0, 70.0]
print(describe(科目="数学", 平均分=85.0))     # 输出：['科目=数学', '平均分=85.0']
groups = [[80, 90], [60, 70, 80]]              # 调用时用 * 拆成两个位置参数
print(all_mean(*groups))                       # 输出：[85.0, 70.0]
kwargs = {"scores": [1, 2, 4], "digits": 1}    # 调用时用 ** 拆成关键字参数
print(summarize(**kwargs))                     # 输出：平均分: 2.3

# 4. 位置-only 与关键字-only 参数（Python 3.8+）
# / 左边的参数只能按位置传；* 右边的参数只能写成 名字=值。签名一眼看清用法，少犯传错位置的错。
def zscore(value, /, *, mu, sigma):
    """标准分 = (value - mu) / sigma。value 只能按位置，mu / sigma 必须写名字。"""
    return (value - mu) / sigma
print(round(zscore(85, mu=80, sigma=5), 2))    # 输出：1.0
# print(zscore(value=85, mu=80, sigma=5))      # 报 TypeError：位置-only 参数不能当关键字传

# 5. 作用域与 LEGB
# 找变量名按 LEGB 顺序：Local（当前函数）-> Enclosing（外层函数）-> Global（模块级）-> Built-in（内置）。
# 函数里"读"全局变量可以；一旦给它赋值，它就地变成本地变量，除非声明 global。
# 内置层是 len / sum / round 这些名字，别在模块里给它们赋值（会挡住内置的），这里不演示。
score_limit = 60        # 全局变量
def is_pass(score):
    """读全局变量没问题，直接读得到。"""
    return score >= score_limit
print(is_pass(75), score_limit)     # 输出：True 60

# global 用来在函数里改全局变量，nonlocal 用来改外层函数的变量。
# 代价：函数会"偷偷"改外部状态，调用顺序一变结果就变，难追踪难测试，能不用就不用。
total_calls = 0
def count_call():
    global total_calls      # 能跑，但属于"有副作用"的函数
    total_calls += 1
count_call(); count_call()
print(total_calls)      # 输出：2
def make_counter():
    """闭包 + nonlocal：counter 在外层函数里，inner 改它。"""
    counter = 0
    def inner():
        nonlocal counter        # 不写 nonlocal，counter += 1 会报 UnboundLocalError
        counter += 1
        return counter
    return inner
next_id = make_counter()
print(next_id(), next_id(), next_id())    # 输出：1 2 3

# 6. 重点陷阱：可变默认参数 def f(x=[])
# 默认值只在函数"定义时"求值一次，之后每次调用都共用同一个对象。
# 所以默认值一旦是列表 / 字典 / set，多次调用就会互相污染。
def collect_wrong(score, box=[]):
    """错的写法：默认值是列表，所有调用者共用它。"""
    box.append(score)
    return box
print(collect_wrong(80))    # 输出：[80]
print(collect_wrong(90))    # 输出：[80, 90]     <- 只想存 90，上次的 80 还赖着
print(collect_wrong(70))    # 输出：[80, 90, 70]

def collect_ok(score, box=None):
    """正确写法：默认值用 None，进函数再新建一个列表。"""
    if box is None:
        box = []
    box.append(score)
    return box
print(collect_ok(80), collect_ok(90), collect_ok(70))    # 输出：[80] [90] [70]   <- 每次都是新列表
# 注意：调用时若真往 box 里传了列表，改的就是外面那个列表（见第 11 节）。

# 7. 函数是一等对象
# 函数和数字、字符串一样，可以赋给变量、当参数传、当返回值返回。
# 把"要做的计算"当参数传进来，是数据处理里的常见写法。
def variance(scores):
    """总体方差：每个数与均值的差平方，再求平均。"""
    mu = mean(scores)
    return sum((x - mu) ** 2 for x in scores) / len(scores)
def spread(scores, stat):
    """按传入的统计函数算一个数：stat 是函数，直接调用它。"""
    return stat(scores)
print(round(spread([2, 4, 4, 4, 5, 5, 7, 9], variance), 2))    # 输出：4.0

# sorted(key=...) 的 key 接收一个函数，把每个元素映射成"排序依据"：先按分数降序，同分按姓名升序
students = [("小明", 88), ("小红", 95), ("小刚", 79), ("小美", 95)]
print(sorted(students, key=lambda item: (-item[1], item[0])))
# 输出：[('小红', 95), ('小美', 95), ('小明', 88), ('小刚', 79)]
# 当返回值也一样：第 5 节的 make_counter 把内层 inner 返回出去，inner 还记着外层的 counter，这就是闭包。

# 8. 数据处理里最常用的几个内置函数
# sum / len 求和与计数；max / min 求最值（key= 可换比较依据）；sorted 排序；round 四舍五入；abs 绝对值。
# 都是内置的，不用 import。
scores = [88, 95, 79, 95, 62]
print(sum(scores), len(scores), round(mean(scores), 1))   # 输出：419 5 83.8
print(max(scores), min(scores))                           # 输出：95 62
print(sorted(scores))                                     # 输出：[62, 79, 88, 95, 95]
print(min(scores, key=lambda s: abs(s - 80)))             # 输出：79
print(abs(-3.5))                                          # 输出：3.5

# 9. 类型注解简述
# 语法：def 名字(参数: 类型) -> 返回类型:。注解只是写给人和工具（mypy 等）看的说明，
# 运行时不会强制检查，传错类型不会自动报错。
def add(a: int, b: int) -> int:
    """返回两个数的和。"""
    return a + b
print(add(1, 2))        # 输出：3
print(add("1", "2"))    # 输出：12      <- 注解没拦住，字符串直接拼起来了

# 10. 常见坑一：在函数里直接改全局变量
# 不加 global 就赋值，Python 认为你要新建局部变量，读它时立刻报 UnboundLocalError。
# 加了 global 能跑，但全局状态被函数悄悄改掉，调用顺序一变结果就变，很难查。
# 更好：要算的值当参数传进去，结果 return 出来。
hits = 0
def bump():
    """错的写法：没声明 global 还想改全局的 hits。"""
    hits += 1        # 一调用就报 UnboundLocalError
    return hits
# bump()   # 取消注释会报：UnboundLocalError: cannot access local variable 'hits' ...

def bump_correct(count):
    """正确写法：进出都靠参数和返回值，不碰全局。"""
    return count + 1
print(bump_correct(0))          # 输出：1

# 11. 常见坑二：列表是引用，不是拷贝
# 列表传进函数后，函数内部原地修改（append / insert / sort）会改到外面那份。
# 想不影响外面，就在函数里先复制：list(scores)（要排序副本就用 sorted(scores)）。
def fill_wrong(scores):
    """在最前面插一个 0 分，直接改了传进来的列表。"""
    scores.insert(0, 0)
    return scores
raw = [80, 90]
print(fill_wrong(raw))      # 输出：[0, 80, 90]
print(raw)                  # 输出：[0, 80, 90]      <- 外面的 raw 也被改了

def fill_ok(scores):
    """先复制再改，不动传进来的原列表。"""
    copied = list(scores)
    copied.insert(0, 0)
    return copied
raw2 = [80, 90]
print(fill_ok(raw2), raw2)  # 输出：[0, 80, 90] [80, 90]   <- 原列表没被动

def make_empty():
    """每次调用都新建一个空列表，两次调用不是同一个对象。"""
    return []
a, b = make_empty(), make_empty()
print(a is b)               # 输出：False
a.append(1)
print(a, b)                 # 输出：[1] []

# 12. 常见坑三：忘了 return，或把 print 当 return 用
# 函数里的 print 只是把字显示出来，调用处拿到的是 None；想拿结果继续算，必须 return。
def mean_print(scores):
    """只打印，不返回。"""
    print(round(sum(scores) / len(scores), 1))
value = mean_print([80, 90])    # 输出：85.0
print(value)                    # 输出：None       <- 后面没法拿它继续算

def mean_return(scores):
    """正确写法：return 出来，调用处随便用。"""
    return round(sum(scores) / len(scores), 1)
print(mean_return([80, 90]))    # 输出：85.0

# 自测题
# 先自己写，写不出来再取消注释看参考答案。

# 1) 写 range_score(scores) 返回极差（最大值减最小值）；空列表返回 0。
# def range_score(scores):
#     return max(scores) - min(scores) if scores else 0
# print(range_score([80, 95, 62]))      # 输出：33

# 2) 写 median_str(scores, digits=1)，返回保留 digits 位小数的中位数字符串。
# 说明：本章没有定义 median，这里自己算一遍（正好练函数 + 条件 + round）。
# def median_str(scores, digits=1):
#     ordered = sorted(scores)
#     mid = len(ordered) // 2
#     if len(ordered) % 2:                       # 奇数个：取正中间
#         m = ordered[mid]
#     else:                                      # 偶数个：取中间两个的平均
#         m = (ordered[mid - 1] + ordered[mid]) / 2
#     return str(round(m, digits))
# print(median_str([3, 1, 4, 2]))       # 输出：2.5
# print(median_str([3, 1, 4, 2], 0))    # 输出：2.0

# 3) 写 total(*groups)，把所有组里的数字加在一起。
# def total(*groups):
#     return sum(n for g in groups for n in g)
# print(total([1, 2], [3, 4], [5]))      # 输出：15

# 4) 写 clamp(value, /, *, low, high)，把 value 限制在 [low, high] 之间（关键字-only 参数）。
# def clamp(value, /, *, low, high):
#     return min(max(value, low), high)
# print(clamp(120, low=0, high=100))     # 输出：100
# print(clamp(-5, low=0, high=100))      # 输出：0

# 5) 用可变默认参数的正确写法：append_tag(tag, tags=None)，两次调用互不影响。
# def append_tag(tag, tags=None):
#     tags = [] if tags is None else tags
#     return tags + [tag]
# print(append_tag("数学"), append_tag("语文"))    # 输出：['数学'] ['语文']

# 6) 用 sorted(key=...) 把 students 按分数降序排，同分按姓名升序。
# students = [("小明", 88), ("小红", 95), ("小刚", 79), ("小美", 95)]
# def rank(students):
#     return sorted(students, key=lambda item: (-item[1], item[0]))
# print(rank(students))     # 输出：[('小红', 95), ('小美', 95), ('小明', 88), ('小刚', 79)]

# 7) bump() 能跑吗？为什么？再改成"进出都走参数和返回值"的写法。
# hits = 0
# def bump():
#     hits += 1        # 一调用就报 UnboundLocalError: cannot access local variable 'hits' ...
# def bump2(count):
#     return count + 1
# print(bump2(0))      # 输出：1
# print(bump())        # 想亲眼看到报错，就把这一行的注释去掉
