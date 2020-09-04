# 根据输入的出生年月日，输出对应生肖和星座

chineseZodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

print(chineseZodiac[0:4])  # 切片操作符：取包含第一到第三的字符，且不含第四个字符

print(chineseZodiac[-1])  # 取包含倒数第一的字符

year = 2018
print(year % 12)
print(chineseZodiac[year % 12])

print('狗' in chineseZodiac)  # 对象[not] in 序列

print(chineseZodiac + 'abcde')  # 序列+序列

print(chineseZodiac * 3)  # 序列*整数

