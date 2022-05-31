#列表

# 格式： 变量名 = []

"""a = []
b = [1,1.1,None,"dd"]
print(a)
print(b)
print("===============")
for x in b:
   print("列表中的值:",x)
"""

c = ["red","black","blue"]
b = [1,1.1,None,"dd"]
c.append("pink")
print(c)
c.reverse()
print(c)
c.extend(b)
print(c)
print("==========")
print(c.count('pink'))
print(c.index('red'))
c.insert(1,"purple")
print(c)

print("===================")
c = ["red","black","blue"]
c.sort()
print(c)

