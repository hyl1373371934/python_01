# 错误和异常

# def div(x,y):
#     z=x/y
#     return z
# print(div(4,1))
# 使用try ... except语句
# 语法格式：
# try：
#     正常代码块
# except Exception as e:
def div(x,y):
    try:
        z = x / y
        return z
    except ZeroDivisionError as e:
        print("不能被0除")
print(div(4,1))
