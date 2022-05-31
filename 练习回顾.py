# print("hello world")
# print(1.2,2,3)
# print(None)
# x=('wae','gfg')
# print(type(x))
# a=10+2
# print(a)
# a,c=10,'s'
# a=10
# b=3
# print(a!=b)
# x=0
# if x>8:
#     print("今天不下雨")
# else:
#     print("今天会下雨")
# a=12
# b=12
# print(a is b)
# c='qqq'
# d='q'
# print(d in c)
# a = '我是一个字符串'
# b = '我是'
# if b in a:
#     print("对了")
# a='abcdefg'
# for x in a:
#     print(x)
# a=0
# while a<5:
#     a +=1
#     print(a)
# sum=0
# for x in range(1,101):
#     sum+=x
# print(sum)
# for x in range(1,11,1):
#     print(x)
#     if x ==7:
#         break
# for x in range(1,11,1):
#     if x ==7:
#         continue
#     print(x)
# a=['dsf',12]
# for x in a:
#     print(x)
# a=['jj','hgjhg']
# b=['dfg','fdg']
# b=a.copy()
# print(b)
# x=(12,'dsf')
# for a in x:
#     print(a)

# a='我的名字是 %s'% ('张三')
# print(a)
# b='我今年 %d岁' % (22)
# print(b)
# c='我买了%+-6.2f元香蕉' % (2)
# print(c)
# d='我买了 {x} 元香蕉,今天星期{y}'.format(x=3,y=2)
# print(d)


# print(a.join(b))
# print(a.split('a'))
# print(a.find('d'))
# sum=0
# a=input("请输入: ")
# for x in a:
#     if x.isnumeric():
#         sum +=1
# print(sum)


# print(a[-2])
# print(a[::2])
# print(max(a),min(a))
# print(sum(a))
# a=[]
# c=list(a)
# print(c)
# a=[]
# for x in range(1,11,1):
#     a.append(x)
# print(a)

# c=[x+10 for x in range(1,11,1) if x%2!=0]
# print(c)
# a=[]
# for x in range(1,11,1):
#     if x%2!=0:
#         x+=10
#         a.append(x)
# print(a)

# def x(a,b):
#     y=a+b
#     return y
# print(x(2,2))

# def add(x,y):
#     z=x+y
#     return x+5
# print(add(8,y=9))

# def x(a,b='python'):
#     print("{}学习{}语言".format(a,b))
# print(x('黄玉龙'))

# def x(x,y,*args):
#     print(args)
#     z=x+y+sum(args)
#     return z
# print(x(2,6,3))

# def x(**kwargs):
#     print(kwargs)
# a={'s':1,'f':2}
# print(x(**a))

# def x(*args,**kwargs):
#     print(args,kwargs)
# b='k'
# a = {'s': 1, 'f': 2}
# print(x(*b,**a))

# class Students():
#     name=""
#     stu=""
#     def __init__(self,stu,name):
#         self.stu=stu
#         self.name=name
#         print("好样的")
#     def study(self):
#         print("{}的{}正在学习软件测试".format(self.stu,self.name))
# s1=Students("积极的","黄玉龙")
# s1.study()

# s1= Students()
# s1.name='黄玉龙'
# s1.stu="积极的"
# print(s1.study())
#
# s2= Students()
# s2.name='李四'
# s2.stu="爱玩的"
# print(s2.study())

# user_list = [{'role':'admin','account':'admin','password':'123456','dept':'tester'}
#     ,{'role':'user','account':'dev','password':'123456','dept':'dev'}]
#
# result={'code':0,'message':''}
#
# def login(username,password):
#     if username is None or username=="":
#         result.update({'code':1,'message':'用户名不能为空'})
#         return result
#     if password is None or password == "":
#         result.update({'code': 1, 'message': '密码不能为空'})
#         return result
#
#
# username=input("请输入用户名")
# password=input("请输入密码")


# def add(x,y):
#     z=x/y
#     return  z
# print(add(4,2))
# def add(x,y):
#     try:
#         z = x / y
#         return z
#     except Exception  as e:
#         print("除法不能被0除情况")
#         print(e)
# print(add(4,0))
# print(add(3,4))
# print(add(4,4))
# try:
#     a=open('a.txt','r')
#     lines=a.readlines()
#     print(4/0)
#     for x in lines:
#         print(x)
#
# except Exception as e:
#     print(e)
#
# finally:
#     print("dad")
#     a.close()
#
def add(x,y):
    try:
        z = x / y
        return z
    except Exception  as e:
        print("除法不能被0除情况")
        print(e)
print(add(4,1))
if __name__ == '__main__':
    print(add(4,2))

