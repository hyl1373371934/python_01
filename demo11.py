"""def 函数名字(参数列表):
     代码块
"""
def add(x,y):
    z = x + y
    return z
print(add(5,5))
# 关键字参数 : 调用时使用key:value形式调用(位置参数在前，关键字参数在后)
# def add(x,y):
#     z=x+y
#     return x+5
# print(add(8,y=9))
# 默认参数 ：其中的某个参数会有默认值，带有默认值的参数放在后面
# def x(a,b='python'):
#     z="{}学习{}语言".format(a,b)
#     return z
# print(x('张三','java'))