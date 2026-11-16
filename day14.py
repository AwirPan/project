import re
s="python itheima itcast python"
res=re.match("python",s)
print(res.group())
print(res.span())