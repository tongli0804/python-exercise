'''
作者：RonyLance
来源：CSDN
原文：https://blog.csdn.net/ronylance/article/category/8100320/1
'''


# Number = 8
# count = 1
# print("---猜猜看andy心中的数字---")
# temp = input('你觉得数字是：')
# while not temp.isdigit():
#     print('不合法，请重新输入')
#     temp = input('请输入：')
# guess = int(temp)
# if guess == Number:
#     print('nice body!')
# if guess < Number:
#     print('这个数字小了')
# if guess > Number:
#     print('这个数字大了')
# while guess != Number and count < 3:
#     temp = input('啊哈，错了，再猜猜：')
#     guess = int(temp)
#     if guess == Number:
#         print("哇，这你都能猜中？")
#         print("不过没有奖励哦！")
#     else:
#         if guess > Number:
#             print('这个数字大了')
#         else:
#             print('这个数字小了')
#     count += 1
# print("游戏结束.")



'''
四舍五入
'''
# # 源代码
# temp = input('输入一个数进行四舍五入：')
# number = float(temp) + 0.5
# resultnumber = int(number)
# print(resultnumber)




'''
请写一个程序打印出 0~100 所有的奇数
'''
# print('100内的奇数有：')
# number = 100
# while number > 0:
#     if number%2 != 0:
#         print(number)
#     number -= 1




'''
爱因斯坦曾出过这样一道有趣的数学题：
有一个长阶梯，若每步上2阶，最后剩1阶；若每步上3阶，最后剩2阶；
若每步上5阶，最后剩4阶；若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩。
题目：请编程求解该阶梯至少有多少阶？
'''
# step = 7   # 台阶数
# i = 1   # 步数
# panduan = 0
# while i <= 100:
#     if (step%2 == 1) and (step%3 == 2) and (step%5 == 4) and (step%6 == 5):
#         panduan = 1
#     else:
#         a = i+1
#         step = 7 * a
#     i += 1
# if panduan == 1:
#     print('阶梯数是：', step)
#     print('步数是：', a)
# else:
#     print('程序限定范围以内无法找到符合答案。')






'''
三元操作符
原版：
1.	x, y, z = 6, 5, 4
2.	if x < y:
3.	    small = x
4.	    if z < small:
5.	        small = z
6.	elif y < z:
7.	    small = y
8.	else:
9.	    small = z
'''
# # 改版
# x, y, z = 6, 5, 4
# small = x if (x < y and x < z) else (y if y < z else z)
# print(small)






'''
题目备忘：按照100分制，90分以上成绩为A，80到90为B，60到80为C，60以下为D，
写一个程序，当用户输入分数，自动转换为ABCD的形式打印。
'''
# score = int(input('请输入一个分数：'))
# if 100 >= score >= 90:
#     print('A')
# elif 90 > score >=80:
#     print('B')
# elif 80 > score >=60:
#     print('C')
# elif 60 > score >=0:
#     print('D')
# else:
#     print('Wrong number !')






'''
 len() 函数从循环前就调用确认出变量值，从而提高代码效率
'''
# i = 0
# string = 'ILoveFishC.com'
# length = len(string)
# while 1 < length:
#     print(i)
#     i += 1







'''
列表推导式或列表解析
列表推导式（List comprehensions）也叫列表解析，灵感取自函数式编程语言 Haskell。
Ta 是一个非常有用和灵活的工具，可以用来动态的创建列表，语法如：
[有关A的表达式 for A in B]
'''
# print([i*i for i in range(10)])
# print([(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0] )
#
# list1 = ['1.Jost do It', '2.一切皆有可能', '3.让编程改变世界', '4.Impossible is Nothing']
# list2 = ['4.阿迪达斯', '2.李宁', '3.鱼c工作室', '1.耐克']
# list3 = []
# for name in list2:
#     for biaoshi in list1:
#         if name[0] == biaoshi[0]:
#             list3.append(name + '：'+biaoshi[2:])
#             list3.reverse()
# for each in list3:
#     print(each)








'''
format函数
'''
# # 通过关键字
# print('{名字}今天{动作}'.format(名字='陈某某', 动作='拍视频'))
# # 通过关键字，可用字典当关键字传入值时，在字典前加**即可
# grade = {'name': '陈某某', 'fenshu': '59'}
# print('{name}电工考了{fenshu}'.format(**grade))
# # 通过位置
# print('{1}今天{0}'.format('拍视频', '陈某某'))
# print('{0}今天{1}'.format('陈某某', '拍视频'))
# # 填充和对齐^<>分别表示居中、左对齐、右对齐，后面带宽度
# print('{:^14}'.format('陈某某'))
# print('{:>14}'.format('陈某某'))
# print('{:<14}'.format('陈某某'))
# print('{:*<14}'.format('陈某某'))
# print('{:&>14}'.format('陈某某'))
# # 精度和类型f精度常和f一起使用
# print('{:.1f}'.format(4.234324525254))
# print('{:.4f}'.format(4.1))
# # 进制转化，b o d x 分别表示二、八、十、十六进制
# print('{:b}'.format(250))
# print('{:o}'.format(250))
# print('{:d}'.format(250))
# print('{:x}'.format(250))
# # 千分位分隔符，这种情况只针对与数字
# print('{:,}'.format(100000000))
# print('{:,}'.format(235445.234235))







'''
编写一个进制转换程序，程序演示如下（提示，十进制转换二进制可以用bin()这个BIF）
'''
# while 1:
#     num = input('请输入一个整数（输入Q结束程序）：')
#     if num.isdigit():
#         num = int(num)
#         print('十进制 -> 十六进制 : %d -> %#x' % (num, num))
#         print('十进制 -> 八进制 : %d -> %#o' % (num, num))
#         print('十进制 -> 二进制 : %d -> ' % num, bin(num))
#     else:
#         if num == 'Q':
#             break
#         else:
#             num = input('输入不合法，请重新输入一个整数（输入Q结束程序）')










'''
练习题
'''
# name = input('请输入带查找的用户名：')
# score = [['迷途', 85], ['黑夜', 78], ['小布丁', 65], ['福禄娃娃', 95], ['意境', 90]]
# for each in score:
#     if name == each[0]:
#         print(name + '的得分是', each[1])
#         break
# if name != each[0]:
#     print('查找的数据不存在！')











'''
计算打印所有参数的和乘以基数（base = 3）的结果
重点：*变量
'''
# def funx5(*numbers):
# 	result = 0
# 	for each in numbers[0:-1]:
# 		result += each
# 	result *= numbers[-1]
# 	print("结果：",result)












'''
寻找水仙花数
题目要求：如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。
例如153 = 1^3 + 5^3 + 3^3，因此153是一个水仙花数。
编写一个程序，找出所有水仙花数。
'''
# def sxhnum():
#     for x in range(100,1000):
#         hund = x // 100
#         ten = (x - hund * 100) // 10
#         zero = (x - hund * 100 - ten * 10)
#         if x == hund**3 + ten**3 + zero**3:
#             print(x)
#         else:
#             continue
#











'''
编写一个函数findstr()，该函数统计一个长度为2的字符串在另一个字符串出现的次数。
例如：假定输入的字符串为“You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted.”，
字符串为“im”，函数执行后打印“子字符串在目标字符串中共出现3次”。

'''
# def findstr(strx,stry):
#     count = 0
#     length = len(stry)
#     if strx not in stry:
#         print('该字符串未在目标字符串中出现！')
#     else:
#         for each in range(length - 1):
#             if stry[each] == strx[0]:
#                 if stry[each+1] == strx[1]:
#                     count += 1
#     print('该字符串在目标字符串中出现了%d次'% count)









'''
编写一个函数，判断传入的字符串参数是否为“回文联”。
回文联，它是我国对联中的一种。用回文形式写成的对联，既可顺读，也可倒读。不仅它的意思不变，而且颇具趣味。
例如：斗鸡山上山鸡斗，龙隐岩中岩隐龙，上海自来水来自海上之类都是 “回文联” 的形式。
'''
# # 方法一：
# def hwlpd(words):
#     length = len(words)
#     count = 0
#     for x in range(length):
#         if words[x] == words[-x - 1]:
#             count += 1
#     if count == length:
#         print('该句子是回文联')
#     else:
#         print('该句子不是回文联')
# # 方法二：
# def hwlpd(words):
#     lista = list(words)
#     listb = list(reversed(words))
#     if lista == listb:
#         print('该句子是回文联')
#     else:
#         print('该句子不是回文联')











'''
编写一个函数，分别统计传入字符串参数（可能不止一个参数）的英文字母、空格、数字和其它字符的个数
'''
# def tongji(*words):
#     length = len(words)
#     for x in range(length):
#         letter = 0
#         space = 0
#         number = 0
#         another = 0
#         ler = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#         spr = ' '
#         nur = '0123456789'
#         for each in words[x]:
#             if each in ler:
#                 letter += 1
#             elif each == spr:
#                 space += 1
#             elif each in nur:
#                 number += 1
#             else:
#                 another += 1
#         print('第 %d 个字符串共有：英文字母 %d 个，数字 %d 个，空格 %d 个，其他字符 %d 个。' % (x + 1, letter, number, space, another))












'''
1、希望在函数中修改全局变量的值，应该使用什么关键字？
    答：使用 global 关键字
    
2、希望在内部函数修改外部函数的局部变量，应该使用什么关键字？
    答：应该用 nonlocal 关键字
'''
# def rlfun():
# 	rlx = 50
# 	def rlfunx():
# 		nonlocal rlx
# 		rlx = 500
# 	rlfunx()
# 	return rlx









'''
Python的函数可以嵌套，但是注意访问的作用域问题
全局外部无法调用一个内嵌的函数，内嵌函数的作用域只存在于它所属的外域函数内。
如果要强行调用的话，要在其外域函数域内先进行调用，然后在全局外部调用外域函数进行使用。
'''
# def outside():
#     print('I am outside!')
#     def inside():
#         print('I am inside!')
#     inside()
# outside()








'''
匿名函数
匿名函数方便于创建一个临时使用的函数，特别是在配合一些BIF（内置函数）使用的时候，
比如说 fliter() 与 map() ，只是临时需要一个函数过程去进行某段代码程序的时候，
匿名函数 lambda 将很方便，不用再去定义命名一个新函数，能够有效地使得代码简洁美观，
也提升了代码书写的工作效率。
'''
'''请将下边的匿名函数转变为普通的屌丝函数？
lambda x : x if x%2 else None
'''
# def funx(x):
#     if x % 2:
#         return x
#     else:
#         return None











'''
列表推导式 与 filter() 和 lambda 组合的不同在于，
列表推导式是按照条件来创建一个列表出来，列表内的元素均符合列表推导式的条件。
而 filter() 和 lambda 组合则是依照条件来将某个集合进行筛选出符合条件的元素加入列表当中。
在一定程度上来说，两者能做到的事情是相同的。

使用filter()和lambda()表达式快速求出100以内所有3的倍数,并改为列表推导式
'''
# list(filter(lambda x : x % 3 == 0 , range(100)))
# # 列表推导式
# [x for x in range(100) if x % 3 == 0]












'''
zip:zip会将两个数以元组的形式绑定在一起
例如：
>>> list(zip([1,3,5,7,9],[2,4,6,8,10]))  
[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)] 
'''
'''
但是如果我希望打包的形式是灵活多变的列表而不是元组
（希望是[[1,2],[3,4],[5,6],[7,8],[9,10]]这种形式），你能做到吗？
（采用map和lambda表达式）
'''
# # 方法一
# list(map(lambda x: list(x), zip([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))
#
# # 方法二
# list(map(lambda x, y: [x, y], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))










'''
递归:
递归的实现是函数自身调用自己进行的，每次函数的调用都需要进行压栈、弹栈、保存和恢复寄存器的栈，
这是非常消耗时间和空间的。另外，如果递归一旦忘记了返回，或者错误的设置了返回条件，
那么执行这样的递归代码就会变成一个无底洞：只进不出。
'''
# def dtbin(num):
#     def tbin(num):
#         result = ''
#         if num:
#             result = tbin( num // 2 )
#             return result + str(num % 2)
#         else:
#             return result
#     if num == 0:
#         return '0b' + '0'
#     else:
#         return '0b' + tbin(num)
# print(dtbin(0))

# def get_digits(n):
#     result = ''
#     if n:
#         result = get_digits(n//10)
#         result += str(n%10)
#     return list(result)
# print(get_digits(554))

# def hwl(words):
#     start = 0
#     end = len(words) - 1
#     def hwlpd(words, start, end):
#         if start > end :
#             return 1
#         else:
#             if words[start] == words[end]:
#                 return hwlpd(words, start + 1, end - 1)
#             else:
#                 return 0
#     if hwlpd(words, start, end):
#         if words[0:len(words)//2] == words[len(words)//2:len(words)]:
#             print('%s 不是一个回文联字符串'%words)
#         else:
#             print('%s 是一个回文联字符串！'%words)
#     else:
#         print('%s 不是一个回文联字符串'%words)












'''
HashMap是一个用于存储Key-Value键值对的集合，每一个键值对也叫做Entry。
这些个键值对（Entry）分散存储在一个数组当中，这个数组就是HashMap的主干。
字典,就是用哈希表实现的。
'''
# print('''|--- 欢迎进入通讯录程序 ---|
# |--- 1：查询联系人资料 ---|
# |--- 2：插入新的联系人 ---|
# |--- 3：删除已有联系人 ---|
# |--- 4：退出通讯录程序 ---|
# ''')
# txl = {}
# while True:
#     srdm = int(input('请输入通讯录功能代码：'))
#     if srdm == 1:
#         xm = input("请输入联系人姓名")
#         if xm in txl:
#             print('为您查到了：' + xm + " 联系电话：" + txl[xm])
#             continue
#         else:
#             print("查询不到此人，为您返回初始界面")
#             continue
#     if srdm == 2:
#         xm = input("请输入联系人姓名")
#         if xm in txl:
#             print('您输入的联系人已存在，' + xm + "联系电话" + txl[xm])
#             pd = input('是否修改联系人？(YES/NO)：')
#             if pd == 'YSE':
#                 dh = input('请输入新的电话号码：')
#                 txl[xm] = dh
#                 print('已经修改成功')
#                 continue
#             else:
#                 print('为您返回初始界面')
#                 continue
#         else:
#             dh = input('请输入电话号码')
#             txl[xm] = dh
#             print('添加完成，为您返回初始界面')
#             continue
#     if srdm == 3:
#         xm = input('请输入联系人姓名：')
#         if xm in txl:
#             print('请问是否删除此联系人？(YES/NO)')
#             pd = input('(YES/NO)：')
#             if pd == 'YES':
#                 del(txl[xm])
#                 print('删除成功，为你返回初始界面')
#                 continue
#             else:
#                 print('为您返回初始界面')
#                 continue
#         else:
#             print('没有找到该联系人，为您返回初始界面')
#             continue
#     if srdm == 4:
#         break
#     else:
#         print('输入有误，为您返回初始界面')
#         continue
'''
编写一个用户登录程序（这次尝试将功能封装成函数）
'''
# def load():
#     dict1 = {'莉莉': 'lili'}
#     while 1:
#         key = input('''
#         |--- 新建用户：N/n ---|
#         |--- 登录帐号：E/e ---|
#         |--- 退出程序：Q/q ---|
#         |--- 请输入指令代码：''')
#         if key == 'N' or key == 'n':
#             temp_name = input('请输入用户名：')
#             while temp_name in dict1:
#                 temp_name = input('此用户名已经被使用，请重新输入：')
#             temp_password = input('请输入密码：')
#             dict1[temp_name] = temp_password
#             print('注册成功！赶紧试试登录吧')
#             continue
#         elif key == 'E' or key == 'e':
#             temp_name = input('请输入用户名：')
#             if temp_name in dict1:
#                 temp_password = input('请输入密码：')
#                 if temp_password != dict1[temp_name]:
#                     temp_password = input('密码错误，请重新输入：')
#                 else:
#                     print('欢迎进入系统，请点右上角的X结束程序！')
#             else:
#                 temp_name = input('没有此用户名，请重新输入：')
#         elif key == 'Q' or key == 'q':
#             break






'''
集合：确保集合内部数字元素的唯一性；集合内的元素是无法索引到的；
集合会自动剔除重复的数字元素；可变集合可以使用 .add() 指令添加一个数字元素，
可以用 .remove() 删除集合内一个数字元素
'''

'''
文件：
默认的打开形式是 'rt' 以 只读 文本 模式打开。其他方式有：
打开模式	执行操作
'r'	以只读方式打开文件（默认）
'w'	以写入的方式打开文件，会覆盖已存在的文件（有风险**）
'x'	如果文件已经存在，使用此模式打开将引发异常
'a'	以写入模式打开，如果文件存在，则在末尾追加写入
'b'	以二进制模式打开文件
't'	以文本模式打开（默认）
'+'	可读写模式（可添加到其他模式中使用）
'U'	通用换行符支持
f.see()需要另外学习一下
'''
# # 编写代码，将文件（OpenMe.mp3）保存为新文件（OpenMe. txt）
# # 第一种方法：
# f1 = open('D:\Python\Python3\OpenMe.mp3')
# f2 = open('D:\Python\Python3\OpenMe.txt', 'x')
# for each_line in f1:
#     f2.write(each_line)
# f1.close()
# f2.close()
# # 第二种方法
# f1 = open('D:\Python\Python3\OpenMe.mp3')
# f2 = open('D:\Python\Python3\OpenMe2.txt', 'x')
# f2.write(f1.read())
# f1.close()
# f2.close()

# # 接受用户的输入并保存为新的文件
# def file_write(file_name):
#     print("请输入内容【单独输入':w'保存退出】：")
#     new_file = open(file_name, 'w')
#     while True:
#         neirong = input()
#         if neirong != ':w':
#             new_file.write('%s\n' % neirong)
#         else:
#             break
# file_name = input('请输入文件名：')
# file_write(file_name)

# 比较用户输入的两个文件，如果不同，显示所有不同处的行号与第一个不同字符的位置
# def file_compare(file_name_1, file_name_2):
#     file_1 = open(file_name_1)
#     file_2 = open(file_name_2)
#     count = 0
#     different = []
#     for each_line in file_1.readline():
#         if each_line == file_2.readline():
#             count += 1
#         else:
#             different.append(count)
#     file_1.close()
#     file_2.close()
#     return different
#     file_name_1 = input('请输入需要比较的第一个文件名：')
#     file_name_2 = input('请输入需要比较的第二个文件名：')
#     file_compare(file_name_1, file_name_2)
#     if len(different) == 0:
#         print('两个文件完全一样')
#     else:
#         print('两个文件有【%d】处不一样' % len(different))
#         for each in different:
#             print('第%d行不一样' % each)

# 当用户输入文件名和行数（N）后，将该文件的前N行中内容打印到屏幕上
# def file_print(file, num):
#     f = open(file)
#     print('''文件%s的前%d的内容如下：''' % (file, num))
#     for i in range(num):
#         print(f.readline())
#     f.close()
# file_name = input('请输入要打开的文件：')
# num = int(input('请输入需要显示该文件前几行'))
# file_print(file_name, num)

# 要求在上一题的基础上扩展，用户可以随意输入需要显示的行数
# def file_print(file ,paragraph):
#     (start, end) = paragraph.split(':')
#     if start == '':
#         start = 1
#     else:
#         start = int(start)
#     if end == '':
#         end = -1
#     else:
#         end = int(end)
#     f = open(file)
#     if start == 1:
#         if end == -1:
#             print('''文件%s的从头开头到结束的内容如下：''' % file)
#         else:
#             print('''文件%s的从开头到第%d行的内容如下：''' % (file, end))
#     else:
#         if end == -1:
#             print('''文件%s的从%d行到结束的内容如下：''' % (file, start))
#         else:
#             print('''文件%s的从第%d行到第%d行的内容如下：''' % (file, start, end))
#     for i in range(start - 1):
#         f.readline()
#     num = end - start + 1
#     if num < 0:
#         print(f.read())
#     else:
#         for i in range(num):
#             print(f.readline())
#     f.close()
# file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
# paragraph = input('请输入需要显示的行数【格式如13：21或：21或21：】：')
# while paragraph == '':
#     paragraph = input('输入有误，请重新输入：')
# file_print(file_name, paragraph)

# 编写一个程序，实现“全部替换”功能
# def file_replace(file_name, rep_word, new_word):
#     f_read = open(file_name)
#     content = []
#     count = 0
#     for each_line in f_read:
#         if rep_word in each_line:
#             count += each_line.count(rep_word)
#             each_line = each_line.replace(rep_word, new_word)
#         content.append(each_line)
#     decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：' \
#                    % (file_name, count, rep_word, rep_word, new_word))
#
#     if decide in ['YES', 'Yes', 'yes']:
#         f_write = open(file_name, 'w')
#         f_write.writelines(content)
#         f_write.close()
#     f_read.close()
# file_name = input('请输入文件名：')
# rep_word = input('请输入需要替换的单词或字符：')
# new_word = input('请输入新的单词或字符：')
# file_replace(file_name, rep_word, new_word)

# 统计当前目录下每个文件类型的文件数
import os
all_files = os.listdir(os.curdir)
type_dict = dict()
for each_file in all_files:
    if os.path.isdir(each_file):
        type_dict.setdefault('文件夹', 0)
        type_dict['文件夹'] += 1
    else:
        ext = os.path.splitext(each_file)[1]
        type_dict.setdefault(ext, 0)
        type_dict[ext] += 1

for each_type in type_dict.keys():
    print('该文件夹下共有类型为【%s】的文件 %d 个' % (each_type, type_dict[each_type]))














