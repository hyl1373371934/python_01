# 1.定义用户默认数据:
user_list = [{'role':'admin','account':'admin','password':'123456','dept':'tester'},{'role':'user','account':'dev','password':'123456','dept':'dev'}]

# 2.定义默认返回结果
result={'code':1,'massage':''}

# 3.定义登录模块
def login(username,password):
    # 用户名或密码为空的情况
    if username is None or username=="":
        result.update({'code':1,'massage':'用户名不能为空'})
        return  result
    if password is None or password == "":
        result.update({'code': 1, 'massage': '密码不能为空'})
        return result

    # 用户登录成功的情况
    for use_info in user_list:
        if username==use_info.get('account') and password==use_info.get('password'):
            result.update({'code':0,'massage':'登录成功','user_list':user_list})
            return  result
    # 用户名或密码不匹配或错误的情况
    result.update({'code':1,'massage':'请检查你的用户名或密码是否填写正确'})
    return result

if __name__ == '__main__':
    username = input("请输入用户名 ：")
    password = input("请输入密码 ：")
    print(login(username,password))

