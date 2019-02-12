#print('Hello world')


#print("我爱你中国")


#a = 20
#b = 30
#c = a + b
#print(c)

#r = 20
#area = 3.1415926 * r * r
#print(area)

"""
from turtle import *        #导入turtle库包

fillcolor("green")                 #配置填充颜色

begin_fill()                       #开始画，类似起笔

while True:                      #开始死循环

    forward(200)              #想画笔向前移动，类似画一个线

    right(144)                   #将画笔移动方向，向右转144度

    if abs(pos()) < 1:         #查看，画笔是否回到原点，（回到原点时，为真）

            break                  #如果回到，原点则跳出循环

end_fill()                         #完成填充图片的绘制。
"""



# a , b = 2 , 3     #同时赋值
# c = a + b
# print(c)


# num = eval(input("请输入一个大于50小于100的数："))
# if 0<= num <= 100:             #if判断后都需要跟一个冒号
#     print("这是对的")
# else:                                    #else后面也需要跟一个冒号
#     print("这是错的")


# n = 3
# while n < 100:                         #注意最后这个冒号
#     print(n, end=" ")                 #end=" "意思是末尾不换行，加空格。
#     n = n + 3


# #输出多组变量
# a = 10
# b = 20
# c = 30
# print("这是a的值{}，这是b的值{}，这是c的值{}".format(a,b,c))


# #"倒背如流"--正序
# s = input("请输入一段文字：")
# i = len(s) - 1
# while i >= 0:
#     print(s[i] , end="")
#     i = i -1



# #“倒背如流”--倒叙
# s = input("请输入一段文字:")
# i = -1
# while i >= - len(s):
#     print(s[i] , end=" ")
#     i = i -1

# #第三章
# #浮点数的计算
# # a = -1.1694737e-03
# a = -1.169477e-03
# print(float(a))


# print("{1}曰：学而时习之，{0}亦说乎。".format("孔子","不"))

# s = "等级考试"
# "{:25}".format(s)


# 判断输入的数是浮点数还是一个整数
# s = eval(input("请输入一个数字："))
# if type(s) == type(123):
#     print("您输入的是一个整数")
# elif type(s) == type(11.3):
#     print("您输入的是一个浮点数")
# else:
#     print("无法判断")


# # 测试if和elif
# num = eval(input("请输入一个数字"))
# if num >= 90:
#     print("真优秀")
# elif 80<= num <90:
#     print("还可以")
# elif num >= 80:
#     print("80分以上了")
# else:
#     print("小于80分啊")



# #成绩
# num = eval(input("请输入你的成绩："))
# if num >= 90:
#     grade = "A"
# elif 80<= num < 90:
#     grade = "B"
# elif 70 <= num <80:
#     grade = "C"
# elif 60 <= num < 70:
#     grade ="D"
# else:
#     grade = "不及格"
# print("你的考试成绩等级是{}".format(grade))


# for c in range(1,30):
#     print(c)



# s = input("请输入几个英文小写字母")
# i = 1
# for c in s:
#     print("这是第{}个字母".format(i) + c)
#     i = i +1



# #while循环
# n = 0
# while n <= 100:
#     print(n)
#     n = n + 3
# else:
#     print("jieshu")



#break

# while True:
#     s = input("请输入一个名字（按Q可退出）：")
#     if s == "Q":
#         break
#     print("您输入的名字是{}".format(s))
# print("已退出程序")



# # 猜数字游戏
# import random
# target = random.randint(1,10000)
# i = 0
# while True:
#     try:
#         s = eval(input("请输入一个1-10000之间你认为可能的数："))
#     except:
#         print("输入有误，此次输入不计入次数")
#         continue
#     i = i + 1
#     if s > target:
#         print("猜大了")
#     elif s <target:
#         print("猜小了")
#     else:
#         break
# print("终于猜对了，你一共猜了{}次,这个数是{}".format(i,target))



# #函数的定义与调用
# def mty(x,y):
#     print(x * y)
# mty(9,2)


# #全局变量
# n = 2
# def mty(x,y):
#     global n                        #使用全局变量n时前面必须加上global
#     n = x * y* n
#     print(n)
# x = eval(input("请输入x的值"))
# y = eval(input("请输入y的值"))
# s = mty(x,y)




# #软文的诗词风训练
# txt = '''
# 人生得意须尽欢，莫使金樽空对月。
# 天生我材必有用，千金散尽还付来。
# '''
# linewidth = 30                        #设定宽度为30
#
# def linesplit(line):                    #这个函数里面的line是形参，通俗讲就是一个挂名的形式参数
#     plist = [',', '，', '.', '。']         #中括号里面是用来查找遍历段中的符号
#     for p in plist:                       #
#         line = line.replace(p, '\n')
#     return line.split('\n')
#
# def linePrint(line):
#     global linewidth
#     print(line.center(linewidth, chr(12288)))
#
# newlines = linesplit(txt)
# for newline in newlines:
#      linePrint(newline)



# #这个简单的例子教我理解split
# line = "da wdw ad aw"
# s = line.split(' ')
# for a in s:
#     print(a)


#第六章--集合类型

# R = { 1010, '1010', 79.8, 12.3, 5}
# S = { 1010, 56.8, '1010', 1010}
# # T = R & S                                             #求交集
# # T = R | S                                              #求并集
# # T = R - S                                              #求差集
# T = R ^ S                                                #求补集
# print(T)



#集合操作函数学习

# R = { 1010, '1010', 79.8, 12.3, 5}
# R.add(123)                                              #集合操作函数add的用法，如果集合中没有123，则插入
# R.remove(79.8)                                       #集合操作函数remove的用法，如果集合中有79.8，则删除
# R.clear()                                                 #集合操作函数clear的用法，清除掉集合中所有的数值
# S = len(R)                                              #集合操作函数len()的用法，遍历集合中元素的个数
# print(S)
# S = 1010 in R                                          #如果1010在R中，print打印True，不在打印False
#S = 1010 note in R
# print(S)





#字典的操作
# d = {"17110901027":"杨鑫","17110901028":"左吉伟"}
# print(d)
# print(d["17110901027"])
# d["17110901027"] = '新杨鑫'
# print(d)
# d["17110901029"] = '刘振宝'
# print(d)
#
# t = len(d)
# print(t)
# q = min(d)
# print



#字典使用的函数--dict
# d = dict()
# print(d)


# d = {"17110901027": "杨鑫", "17110901028": "左吉伟"}
# # t = d.keys()
# # t = d.values()
# # t = d.items()
# # print(t)
# for k in d:
#     print("学号{}对应的名字是{}".format(k,d.get(k)))


# #哈姆雷特例子----垃圾版 日后完善
# PATH = "H:\\"
# def getTxt():
#     txt = open(PATH + "english.txt","rt").read()
#     txt = txt.lower()
#     for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~' :
#         txt = txt.replace(ch, "")
#     return txt
# EnglistTxt = getTxt()
# words = list(EnglistTxt)
# counts = {}
# for word in words:
#     counts[word] = counts.get(word,0) + 1
# print(counts)



#理解readlne()函数和读取指针
# PATH = "H:\\"
# txt = open(PATH + "test.txt","r")
# s = txt.readline()
# t = txt.readline()
# txt.seek(0)
# r = txt.readline()
# print(s)
# print(t)
# print(r)
# txt.close()                                      #关闭文件




#文件的逐行读取
# PATH = "H:\\"
# txt = open(PATH + "test.txt","r")
# for line in txt:
#     print(line)
# txt.close()



#关于文件的读写write函数
# PATH = "H:\\"
# txt = open(PATH + "test.txt","w")                               #注意“w”，给予”写“的权限
# txt.write('出面不觉晓，处处闻啼鸟。\n')
# txt.write('举头望明月，低头思故乡。\n')
# txt.close()
# txt = open(PATH + "test.txt","r")
# for line in txt:
#     print(line)
# txt.close()

# a = 1
# b = 2
# c = 3
# a,b,c = b,a,c
# print(a,b,c)


import requests

r = requests.get("http://www.baidu.com")
r.status_code
r.text