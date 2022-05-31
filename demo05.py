#  字典

#  定义 ：  d = {key1:value1,key2:value2}


d={'1':'北京','2':'李四'}
print(d)

#  字典值的获取 : 字典["键名"]
print(d['1'])
d['name'] = '王五'
print(d)
print(d.get('class'))
q={'3':'北京','4':'李四'}
d.update(q)
print(d)
print('2' in d)
print('===========')
print(d.keys())
print(d.values())
print(d.keys())
print("获取字典中的键值对:",d.items())
print('=====================')
for x in d.keys():
    print(x)
for x,y in d.items():
    print(x,'====',y)


