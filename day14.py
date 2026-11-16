import re
s="1python itheima itcast python"
res=re.search("python",s)
print(res.group())
print(res.span())