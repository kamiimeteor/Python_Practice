# 根据输入的出生年月日，输出对应星座

zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')

zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))  # 元组当中内容是不可变更的

# 列表当中内容是可以变更的 [0, "abcd"]

(month, day) = (2, 15)

# filter功能
zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
# print(zodiac_day) - <filter object at 0x7fa8180225e0>
zodiac_len = len(list(zodiac_day)) % 12
list(zodiac_day)  # [(1, 20)]
print(len(list(zodiac_day)))  # 0???
print(zodiac_len)  # 1
print(zodiac_name[zodiac_len])

'''
filter(function, iterable)
  lambda匿名函数的格式：冒号前是参数，可以有多个，用逗号隔开，冒号右边的为表达式。
  
def sum(x,y):
    return x+y
print(sum(4,6))

f=lambda x,y:x+y
print(f(4,6))
这俩个例子的效果是一样的，都是返回x+y

a=lambda x:x*x
print(a(4))  #传入一个参数的lambda函数 返回x*x

b=lambda x,y,z:x+y*z
print(b(1,2,3))  #返回x+y*z  即1+2*3=7

*方法结合使用
foo=[2, 18, 9, 22, 17, 24, 8, 12, 27]
print(list(filter(lambda x:x%3==0,foo))) #筛选x%3==0 的元素 [18, 9, 24, 12, 27]
print(list(map(lambda x:x*2+10,foo)))    #遍历foo 每个元素乘2+10 再输出

'''

#列表的定义
a_list = ['abc', 'xyz']
a_list.append('X')  #列表中增加元素
print(a_list)
a_list.remove('xyz')
print(a_list)  #列表中删除元素