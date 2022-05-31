user_list = [{'role':'admin','account':'admin','password':'123456','dept':'tester'}
    ,{'role':'user','account':'dev','password':'123456','dept':'dev'}]
x=user_list[0]
y=user_list[1]
a=input("输入用户名: ")
b=input("输入密码: ")
while a =="" or b=="" :
    print("登录失败，用户名或密码不能为空")
    a = input("输入用户名: ")
    b = input("输入密码: ")
while a!=x.get('account') and a!=y.get('account'):
    print("登录失败，请检查您的用户名或密码是否填写正确")
    a = input("输入用户名: ")
    b = input("输入密码: ")
if a==x.get('account') and b==x.get('password'):
    print({'code':0,'message':'登录成功'},x)
elif a==y.get('account') and b==y.get('password'):
    print({'code': 0, 'message': '登录成功'},y)
else:
    i=0
    for i in range(0,4):
        print("登录失败，请检查您的用户名或密码是否填写正确")
        a = input("输入用户名: ")
        b = input("输入密码: ")
    print("输错5次，账号锁定")
