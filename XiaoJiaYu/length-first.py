'''
请用已学过的知识编写程序，统计下边这个长字符串中各个字符出现的次数并找到小甲鱼送给大家的一句话
'''
str1 = "~!@#$%^&*()_+/,.?<>;:[]|\{}"
lists = []
count_empty = 0
pp = ''
for i in open("length-first.txt"):
    if i == '\n':
        count_empty += 1
        i = i.rstrip('\n')
    pp = pp + i

for each in str1:
    key = pp.count(each)
    if key != 0:
        print('%s 有：%d 个' % (each, key))

# for y in pp:
#     if y not in str1:
#         lists.append(y)
# print('\\n 有：%d 个' % count_empty)
# print('小甲鱼要告诉我们的话是：' + ''.join(lists))
