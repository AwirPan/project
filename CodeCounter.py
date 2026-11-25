import os

# 1. 想办法把 project 文件夹里的文件名一个个拿出来
# 2. 判断文件名是不是 .py 结尾
# 3. 是就 print 出来
data=os.listdir()
for file in data:
    temp=file[-1:-4:-1]
    if temp=="yp.":
        print(file)
