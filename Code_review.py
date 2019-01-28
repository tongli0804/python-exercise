'''
写一个密码安全性检查的脚本代码
低级密码要求： 
# 1. 密码由单纯的数字或字母组成 
# 2. 密码长度小于等于8位

# 中级密码要求： 
# 1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合 
# 2. 密码长度不能低于8位 

# 高级密码要求： 
# 1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合 
# 2. 密码只能由字母开头
# 3. 密码长度不能低于16位
---------------------
作者：RonyLance
来源：CSDN
原文：https://blog.csdn.net/RonyLance/article/details/82935558
版权声明：本文为博主原创文章，转载请附上博文链接！
'''

spachars = '~!@#$%^&*()_=-/,\.?<>;:[]{}|'
numbers = '0123456789'
chars = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
choose = 'y'
print('=======RonyLance密码安全级别检测=======')
# 开启循环保障测试有循环运行选择
while choose == 'y':
    password = input('请输入你的密码进行检查：')
    length = len(password)
    # 空白监测提示
    while password.isspace() or length == 0:
        password = input('你输入的密码为空，请重新输入：')
        length = len(password)
    # 长度检测
    if length <= 8:
        flag_len = 1
    elif 8 < length < 16:
        flag_len = 2
    else:
        flag_len = 3
    # 属性检测
    flag_each = 0
    for each in password:
        if each in spachars:
            flag_each += 1
            break
    for each in password:
        if each in numbers:
            flag_each += 1
            break
    for each in password:
        if each in chars:
            flag_each += 1
            break
    # 级别测定
    while 1 :
        print("你的密码安全级别为：", end='')
        if flag_len == 1 or flag_each == 1:
            print('低级')
        elif flag_len == 2 or flag_each == 2:
            print('中级')
        elif flag_len == 3 or flag_each == 3:
            print('高级')
        else:
            print('你的密码不符合规范，请按照标准重新设置')
        break
    choose = input('如需继续经输入“y”继续：')



