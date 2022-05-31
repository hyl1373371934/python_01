
user_list = [{'role': 'admin', 'account': 'admin', 'password': '123456', 'dept': 'tester'}
, {'role': 'user', 'account': 'dev', 'password': '123456', 'dept': 'dev'}]
x = user_list[0]
y = user_list[1]
a=input("输入用户名: ")
b=input("输入密码: ")
if a==x.get('account') and b==x.get('password'):
    print({'code':0,'message':'登录成功'},x)
    a = input("输入用户名: ")
    if a==x.get('account'):
        del x['password']
        x1 = x
        print(x1)
    else:
        print("无查询结果的提示")
elif a==y.get('account') and b==y.get('password'):
        print({'code': 0, 'message': '登录成功'},y)
        a=input("输入用户名: ")
        if a == y.get('account'):
            del y['password']
            y1 = y
            print(y1)
        else:
            print("无查询结果的提示")
else:
        print("权限不足")







