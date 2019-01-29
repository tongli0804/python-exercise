'''
请用已学过的知识编写程序，找出小甲鱼藏在下边这个长字符串中的密码，密码的埋藏点符合以下规律：
a) 每位密码为单个小写字母
b) 每位密码的左右两边均有且只有三个大写字母
'''
new_string = ''
for i in open("length-sce.txt"):
    i = i.strip('\n')
    new_string = new_string + i

countA = 0
countB = 0
countC = 0
target = 0
length = len(new_string)

for i in range(length):
    if new_string[i].isupper():
        if countB == 1:
            countC += 1
            countA = 0
        else:
            countA += 1
        continue
    if new_string[i].islower() and countA == 3:
        countB = 1
        countA = 0
        target = i
        continue
    if countC == 3 and countB == 1:
        print(new_string[target], end='')

    countA = 0
    countB = 0
    countC = 0

# 输出：
# ilovefishc



