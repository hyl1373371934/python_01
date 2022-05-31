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


# 创建一个类，包括新增用户，修改用户，删除用户，查询用户
class User():


    # 用户查询功能
    def get_user(username):


        # 判断用户名是否登录，若登陆成功可以进行查询；若登陆失败，返回权限不足
        if  result.get('code')!=0:
            result.update({'code':11,'massage':'用户未登录，无法查询结果'})
            return  result
        # 输入用户名进行查询，返回结果(支持模糊查询)
        result.update({'user_list':[]})
        lst=[]   # 存放的是查询到的结果的数据
        for x in user_list:
           account=x.get('account')
           if username in account:    #支持模糊查询
                x.pop('password')
                lst.append(x)

        # 判断新列表里的数据，如果列表不为空，查询成功，返回对应结果
        if lst:
            result.update({'massage':'查询用户成功!','user_list':lst})
            return result

        # 若输入的用户名不正确，返回无查询结果提示
        result.update({'code':12,'massage':'未查询到用户，请重新输入'})
        return result

    if __name__ == '__main__':
        # 进行循环，以使用户做各种操作
        flag=True
        while flag:
            # 提供用户的各种选择，比如输入1代表登录操作，输入2代表查询操作，输入q：推出操作
           vls= input('操作请输入对应编号:' 
                '\n''1:) 进行登录:'
                '\n''2:) 进行查询用户，请输入用户名:'
                '\n''q:) 退出操作:'
                '\n''其他字符:) 未知操作，请重新输入:')

            # 当输入未知符号后，进行重新登录
           if not vls in ('1','2','q','quit'):
                    print("="*30)
                    continue


           # 进行登录操作
           if vls=='1':
                username = input("请输入用户名 ：")
                password = input("请输入密码 ：")
                login.result=login(username,password)
                print(login.result)
                print("="*30)
                continue

           # 进行用户查询的情况
           if vls=='2':
            name=input("请输入查询用户名:")
            get_result=get_user(name)
            print(get_result)
            print("=" * 30)
            continue
            # 是否退出
           if vls in('q','quit'):
               flag=False
               print("退出成功!")







