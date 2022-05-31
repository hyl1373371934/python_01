""" for 循环变量 in 序列
     代码块
"""
for z in "abcdef":
    print(z)
"""
while 条件语句(condition)：
代码块(statements)……

"""
print("===========")
a = 1
sum=0
while a <= 100:
   sum += a
   a += 1
print(sum)
"""
range(start,end,step)
"""
print("===========")
for x in range(1,11,1):
   print(x)
   if x == 7:
       break
print("===========")
for x in range(1,11,1):
    if x == 7:
        continue
    print(x)