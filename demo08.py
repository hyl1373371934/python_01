# 格式化字符串 :%s
my_str = "my name is %s" % ('李四')
print(my_str)

# 格式化整数 : %d
my_str1 ="我今年 %d 岁" % (22)
print(my_str1)

# 格式化浮点数 : %f
my_str2 ="一斤苹果%f元" % (5)
print(my_str2)

# 辅助指令 : m.n
my_str3 = "一斤苹果%4.2f元" % (6)
print(my_str3)

# 显示左对齐 : -
my_str4 = "一斤苹果%-9.2f元" % (6)
print(my_str4)

# 数字显示+ : +
my_str5 = "一斤苹果%+4.3f元" % (6)
print(my_str5)

# 前面显示0 : 0
my_str6 = "一斤苹果%09.3f元" % (6)
print(my_str6)

# 使用format()进行格式化  '{}'.format('字符串')
my_str7 = "张三 今年 {} 岁".format(25)
print(my_str7)

# 使用format()格式化两个参数  '{}  {}'.format(参数1,参数2)
my_str8 = "今天星期{},张三买了{}斤苹果".format('一',5)
print(my_str8)

# format位置参数 : "{0}{1}{2}".format(第一个数,第二个数,第三个数)
my_str9 = "今天星期{0},张三买了{2}斤苹果".format('一',5,3)
print(my_str9)

# format关键字参数 : "{x}{y}".format(x='1',y='2')
my_str10 = "今天星期{x},张三买了{y}斤苹果".format(x='1',y='2')
print(my_str10)
