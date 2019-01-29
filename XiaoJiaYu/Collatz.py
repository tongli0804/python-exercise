'''
作者：RonyLance
来源：CSDN
原文：https://blog.csdn.net/RonyLance/article/details/82938030
版权声明：本文为博主原创文章，转载请附上博文链接！
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














