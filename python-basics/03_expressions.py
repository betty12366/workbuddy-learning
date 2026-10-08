"""第 3 章 表达式

本章讲什么：
    表达式和语句的区别；条件表达式；列表/字典/集合推导式与生成器表达式；
    解包赋值；海象运算符 :=（Python 3.8+）；lambda；f-string 里的表达式与格式说明符。

学完能做什么：
    用一行推导式替代"建空列表 + for + append"；把两列数据打包拆包；
    格式化输出成绩表；写 lambda 当排序 key；并避开 3 个常见的表达式坑。

怎么跑：
    python 03_expressions.py
"""

# 1. 表达式和语句

# 表达式：有值能求值，可以放进 print()、赋值右边、函数参数。
# 语句：执行一个动作没有值。赋值、if、for、import、def 都是语句。
scores = [88, 45, 92, 67, 59, 73, 100, 38, 81, 60]
average = sum(scores) / len(scores)         # 赋值是语句，右边是表达式
print(average, sum(scores) / len(scores))   # 表达式能直接打印，语句不行
# 输出：70.3 70.3

# 2. 条件表达式（三元表达式）

# 写法：值1 if 条件 else 值2
score = 58
print("及格" if score >= 60 else "不及格")
# 输出：不及格
# 嵌套三元能跑，但要一层层往里剥，难读；三个以上分支请写 if/elif。
grade = "优秀" if score >= 90 else "及格" if score >= 60 else "不及格"
print(grade)
# 输出：不及格

# 3. 列表推导式（对比 for 循环）

# 循环写法：3 行代码，重点被"建空列表 / append"冲淡
doubled = []
for s in scores:
    doubled.append(s * 2)
print(doubled)
# 输出：[176, 90, 184, 134, 118, 146, 200, 76, 162, 120]
# 推导式写法：一句话说清"对每个元素做什么"，结果完全等价
print([s * 2 for s in scores] == doubled)
# 输出：True

# 4. 带条件的推导式：过滤 + 变换

# 口诀：变换写最前，过滤写中间，迭代写最后
print([s for s in scores if s >= 60])
# 输出：[88, 92, 67, 73, 100, 81, 60]
# 变换 + 过滤：只给不及格的加 5 分
print([s + 5 for s in scores if s < 60])
# 输出：[50, 64, 43]
# 过滤 + 变换 + 三元：直接把分数转成等级
print(["及格" if s >= 60 else "不及格" for s in scores[:4]])
# 输出：['及格', '不及格', '及格', '及格']

# 5. 嵌套推导式（矩阵转置）

# 3 个学生、4 次测验的分数表，行 = 学生
table = [[80, 90, 85, 70], [60, 65, 58, 72], [95, 88, 92, 100]]
# 循环写法：外层遍历列号，内层取这一列的每个人
t_loop = []
for col in range(4):
    t_loop.append([row[col] for row in table])
print(t_loop)
# 输出：[[80, 60, 95], [90, 65, 88], [85, 58, 92], [70, 72, 100]]
# 一行转置：for 的顺序和嵌套循环一致，先写外层再写内层
transposed = [[row[col] for row in table] for col in range(4)]
print(transposed)
# 输出：[[80, 60, 95], [90, 65, 88], [85, 58, 92], [70, 72, 100]]

# 6. 字典推导式和集合推导式

# 字典推导式 {键: 值 for ...}：把两列数据打包成映射
ids, first_round = ["S01", "S02", "S03"], [88, 45, 92]
score_map = {sid: s for sid, s in zip(ids, first_round)}
print(score_map)
# 输出：{'S01': 88, 'S02': 45, 'S03': 92}
# 带过滤：只留及格的
print({sid: s for sid, s in score_map.items() if s >= 60})
# 输出：{'S01': 88, 'S03': 92}
# 集合推导式：自动去重，常用来数"有哪些不同的值"
print(sorted({g for g in ["A", "B", "B", "C", "A"]}))
# 输出：['A', 'B', 'C']

# 7. 生成器表达式（惰性、省内存）

import sys

# 语法：把列表推导式的 [] 换成 ()，但不会立刻算出所有结果
gen = (s * 2 for s in scores[:4])
print(type(gen).__name__)
# 输出：generator
# 惰性求值：用 next() 要一个算一个
gen = (s * 2 for s in scores[:4])
print(next(gen), next(gen))
# 输出：176 90
# 内存差别：列表先建出所有元素，生成器只建一个对象
big = list(range(100_000))
print(sys.getsizeof(x * 2 for x in big) < sys.getsizeof([x * 2 for x in big]))
# 输出：True
# 只遍历一遍时最划算：直接喂给 sum / any / all
print(sum(s * 2 for s in scores))
# 输出：1406
# 取舍：需要 len / 索引 / 反复遍历 -> 列表推导式；只跑一遍 -> 生成器表达式

# 8. 解包赋值

# 交换：右边先算成一个元组再按位置赋回，不需要临时变量
a, b = 3, 7
a, b = b, a
print(a, b)
# 输出：7 3
# 平行解包 + zip(*pairs)：把"学号-分数"两列拆开
pairs = [("S01", 88), ("S02", 45), ("S03", 92)]
pair_ids, pair_scores = zip(*pairs)
print(pair_ids, pair_scores)
# 输出：('S01', 'S02', 'S03') (88, 45, 92)
# 星号解包：第一个单拎出来，其余打包成列表
first, *rest = scores
print(first, rest)
# 输出：88 [45, 92, 67, 59, 73, 100, 38, 81, 60]
# 嵌套解包：左右结构要对齐
sid, (m1, m2, m3) = ("S03", [95, 88, 92])
print(sid, m1 + m2 + m3)
# 输出：S03 275

# 9. 海象运算符 :=（Python 3.8+）

# 解决的问题：表达式的值存进变量，同时参与判断，不用算两遍。
# 老写法要在 if 内外各调一次 len：
data = [3, 5, 7, 9, 11]
if (n := len(data)) > 3:          # 海象：算一次，结果留在 n 里
    print("长度", n)
# 输出：长度 5
# 推导式里最有用：过滤用的中间值可以直接留下来
raw_scores = [88, 45, 92, 67]
print([c for s in raw_scores if (c := s + 5) >= 70])
# 输出：[93, 97, 72]
# 读一行处理一行：读取和判断合成一步，读到空串就停
it = iter(["88", "45", "92", ""])
while (line := next(it, "")):
    print("读到", line)
# 输出：
# 读到 88
# 读到 45
# 读到 92

# 10. lambda 表达式

# lambda 只能装一个表达式，返回值就是它的值
to_grade = lambda s: "及格" if s >= 60 else "不及格"
print(to_grade(72), to_grade(50))
# 输出：及格 不及格
# 取舍：只用一次、一个表达式 -> lambda；要名字、要复用、多行分支 -> def
def to_grade_def(s):
    return "及格" if s >= 60 else "不及格"
print(to_grade(72) == to_grade_def(72))
# 输出：True
# lambda 的主场：当排序/分组的 key，用过就丢
pairs = [("S01", 88), ("S02", 45), ("S03", 92)]
print(sorted(pairs, key=lambda p: p[1]))
# 输出：[('S02', 45), ('S01', 88), ('S03', 92)]

# 11. f-string 里的表达式

name, one_score = "小明", 87.5
# 花括号里能放变量、任意表达式、函数调用
print(f"{name} 的分数是 {one_score}")
# 输出：小明 的分数是 87.5
print(f"名字长度 {len(name)}，全班平均 {sum(scores) / len(scores)}")
# 输出：名字长度 2，全班平均 70.3
# 格式说明符写在冒号后面
print(f"{one_score:.2f}")
# 输出：87.50
print(f"{one_score:>8.2f}|")
# 输出：   87.50|
print(f"{1234567:,}", f"{0.873:.1%}")
# 输出：1,234,567 87.3%
# 拼成绩表：学号左对齐，分数和百分比右对齐
rows = [("S01", 88.456), ("S02", 45.2), ("S03", 92.0)]
for sid, s in rows:
    print(f"{sid:<5} {s:>7.2f} {s / 100:>7.1%}")
# 输出：
# S01     88.46   88.5%
# S02     45.20   45.2%
# S03     92.00   92.0%

# 12. 常见坑一：循环里创建 lambda 的延迟绑定

# lambda 体里的 i 在"调用时"才去查，循环结束后 i 只剩最后一个值
funcs = []
for i in [1, 2, 3]:
    funcs.append(lambda: i)
print([f() for f in funcs])
# 输出：[3, 3, 3]
# 修法：默认参数在定义时就求值，把当前 i 固定住
funcs = []
for i in [1, 2, 3]:
    funcs.append(lambda i=i: i)
print([f() for f in funcs])
# 输出：[1, 2, 3]

# 13. 常见坑二：推导式的变量作用域

# Python 3 里推导式有独立作用域：读得到外层变量，写进去的出不来
s = "外层的 s"
print([s for s in scores[:3]])
# 输出：[88, 45, 92]
print(s)
# 输出：外层的 s
# 对比：普通 for 循环的变量会留在当前作用域
for t in scores[:3]:
    pass
print(t)
# 输出：92

# 14. 常见坑三：生成器只能遍历一次

# 生成器是一次性迭代器，取完就空了
gen = (s for s in scores[:3])
print(list(gen))
# 输出：[88, 45, 92]
print(list(gen))
# 输出：[]
# 被 sum / any 消费过之后同样没内容
gen2 = (s for s in scores[:3])
print(sum(gen2), sum(gen2))
# 输出：225 0
# 修法：包成函数，每次调用都新建一个生成器；需要反复用就直接用列表推导式
def score_stream():
    return (s for s in scores[:3])
print(list(score_stream()), list(score_stream()))
# 输出：[88, 45, 92] [88, 45, 92]

# 自测题：先自己写答案，再把下面的注释取消掉运行对照

tests = [52, 61, 88, 95]
# 1) 列表推导式：每个分数加 3 -> [55, 64, 91, 98]
# assert [t + 3 for t in tests] == [55, 64, 91, 98]
# 2) 带过滤的推导式：只留 >= 60 -> [61, 88, 95]
# assert [t for t in tests if t >= 60] == [61, 88, 95]
# 3) 嵌套推导式：转置 [[1, 2], [3, 4]] -> [[1, 3], [2, 4]]
# assert [[r[c] for r in [[1, 2], [3, 4]]] for c in range(2)] == [[1, 3], [2, 4]]
# 4) 字典推导式：只留及格的键 -> {"b": 61}
# assert {k: v for k, v in {"a": 52, "b": 61}.items() if v >= 60} == {"b": 61}
# 5) 生成器表达式：2 倍分数求和 -> 592
# assert sum(t * 2 for t in tests) == 592
# 6) 星号解包：first == 52，rest == [61, 88, 95]
# first, *rest = tests
# assert first == 52 and rest == [61, 88, 95]
# 7) f-string 格式说明符：61 分 -> "61.0%"
# assert f"{61 / 100:.1%}" == "61.0%"

print("本章结束：把自测题的注释逐条取消，验证你的答案")
# 输出：本章结束：把自测题的注释逐条取消，验证你的答案
