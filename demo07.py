# 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
a = 1
b = 2
c = 3
d = 4
print("结果:",a+b-c*d)
# 2. 打印1~100内被3整除的所有数的和
sum = 0
a = 3
while a <= 100:
    sum += a
    a += 3
print(sum)
# 3. 使用range()输出1~10内的所有奇数
for x in range(1,11,2):
    print(x)
# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
sum1 = 0
sum2 = 0
for a in range(2,101,2):
     sum1 += a
for a in range(1,101,2):
     sum2 += a
print(sum1-sum2)
# 5. 求1+2+3+...+100的和
a = 1
sum = 0
while a <= 100:
    sum += a
    a += 1
print(sum)
# 6. 判断一个数n能同时被3和5整除
n= int(input("请输入一个数字: "))
if n%3==0 and n%5==0:
    print("能被3和5整除")
else:
    print("不能被3和5整除")
# 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
x = int(input("输入一个变量: "))
if x in range(1,101,1):
    print(x)
# 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
x = int(input("输入整数x: "))
y = int(input("输入整数y: "))
z=  int(input("输入整数z: "))
a = [x,y,z]
a.sort()
print(a)
# 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
a = int(input("score: "))
if a >= 90:
    print("A")
elif 60 <= a <= 89:
    print("B")
else:
    print("C")
# 10. 将一个列表的数据复制到另一个列表中。
a = [2,"qq"]
b = [3,None,"ww"]
a.extend(b)
print(a)

# 11. 输出 9*9 乘法口诀表
for x in range(1,11,1):
    for y in range(x,x+1):
        print(x,"*",y,"=",x)
# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
str=input('请输入：')
letter=0
num=0
other=0
for i in str:
    if i.isdigit():
        num += 1
    elif i.isalnum():
        letter += 1
    else:
        other += 1
print(letter,num,other)
# 13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个)
a = int(input('请输入数字'))
b = int(input('请输入相加个数'))
s, s_sum = 0, 0
for x in range(b):
    s += a * 10 **(x)
    s_sum += s
print(s_sum)
