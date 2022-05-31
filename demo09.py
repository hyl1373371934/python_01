# 字符串演示
# 1. 连接字符串分 : join(seq)
astr ="="
bstr =astr.join("world")
print(bstr)

# 2.分割字符串 : split(str=""),str代表分割符
cstr ="helloworldphpjavapython"
dstr =cstr.split("o")
print(dstr)

# 查找字符串 :find(substr) ,找到了返回最小索引,没有找到返回-1
estr="helloworldphpjavapython"
print(estr.find("z"))

# 查找以xxx结尾的字符串 : endwith("xxx")
fstr ="hello.doc"
if fstr.endswith(".doc"):
 print("好样的")

# 替换字符串  replace(old,new)
gstr = "hello python"
hstr=gstr.replace("python","c")
print(hstr)

# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数

sum=0
a= input("请输入: ")
for x in a:
 if x.isdigit():
  sum +=1
print(sum)
