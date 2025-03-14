print('hello world')
print('hello world')
print('hello world')
print('hello world')
print('hello world')
print('hello world')#这个是单行注释
print('hello world')
'''我是多行注释 
第二行注释1
'''
# 输出函数print()
print('哈哈哈','嘿嘿嘿','嘻嘻嘻',sep='.')
print('hello',end='8' )
print('sensen')
 #1.变量的作用
 # 计算机的储存空间，用于保存数据
 #2.定义变量的格式
 #变量名 = 值
#注意：=是赋值运算符，左后两边打上空格是为了代码的规范，美观性
num1 = 3 #num1就是一个变量，保存可乐的价格
num2 = 4 #num1就是一个变量，保存冰激凌的价格
total = num1 + num2 #total也是一个变量，保存总价格
print(num1)
#加上引号会打印引号里面的内容，没有引号就会被识别成变量名，打印的是变量的值，如果该变量没有被赋#报命名错误
#变量只有再赋值以后才会被创建，所以使用变量之前必须要赋值
print(num2)
a = 666
b = a
print(b)
a = 999 # 同一个值可以反复赋值，可以是不同的数据类型，文字等
print(a)

# 2.标识符
# 2.1 只能由数字，字母，_组成
six = 1
six2 = 1
six_ = 1
#2.3变量的命名规范
#1.见名知义
#name = "sen"
#2.下划线分割法：（python常用变量名命名规则）
#user_name = "sen"
#3 数值类型
#3.1 int整型常用：任意大小的整数
# num = 66
#检测数据类型的方法 type()
#3.2 float 浮点型：小数
#3.3 bool布尔型，重点，通常用于判断
#有固定写法，一个为True(1)为False(0)
print(True + False)
#3.4 complex 附属型
#4.转义字符
# 4.1\t制表符通常表示空四个字符，也称缩进# print('sixs\tar')
print("姓名\t年龄\t电话")
# 4.2 \n换行符表示将当前位置移到下一行开头 print('哈哈\n嘻嘻’)
# 4.3 \r回车表示将当前位置移到本行开头# print("six\rsdhdfh"))
# 4.4\\反斜杠符号 print('sixs\\tar')

#1.if判断基本格式
#if 判断条件：
#  满足条件做的事情
# #用户从控制台输入成绩，如果满分，输出"你真棒!”，如果60分，输出"还要继续加油哈!”
# score = input("请输入成绩:")
# if score == "100":
#     print("你真棒！")
# if score == "60":
#     print("还要继续加油哈！")

# if-else
a = 666
if a == 666:
    print("你真棒")
else: #else后面不需要加任何条件
    print("还要继续加油")
# 三目运算(三元表达式)
#基本格式:为真结果if判断条件 else为假结果
a = 8
b = 5
if a <= b:
    print("a小于等于b")
else:
    print("a比b大")

score = 412
if 85 <= score <= 100:
    print("优秀")
elif 60 <= score <= 85:
    print("及格")
elif 0 <= score < 60:
    print("不及格")
else:
    print("分数无效")