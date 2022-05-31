 # 序列的通用操作
#   索引 - 列表,序列,字符串,元组
lst =['a',123,None]
print(lst[-2])
print(lst[1])

tp = (1,2,'sad')
print(tp[0])

my_str='gdgdfgfdg'
print(my_str[0])
print(my_str[-9])

# 2.序列,字符串,元组的切片 : seq[[start:end:step],start代表位置,默认从0开始
lst1=["fghfgh",123,None,12]
tp1 = (10,20,'sad','jkjh','gg')
my_str1='gdgdfgfdg'
print(lst1[1:3:1])
print(tp1[1:3:1])
print(my_str1[4:6:1])
print(my_str1[2:6:1])


# print('='*60)
# a=[1,7,74]
# print(max(a),min(a))
# a=[1,2,3]
# b=str(a)
# for x in b:
#     print(x)

# a=[]
# for x in range(1,11,1):
#     a.append(x)
# print(a)

c=[x+10 for x in range(1,11,1) if x%2]
print(c)



