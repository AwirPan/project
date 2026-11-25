import os

# 1. 想办法把 project 文件夹里的文件名一个个拿出来
# 2. 判断文件名是不是 .py 结尾
# 3. 是就 print 出来
path=r"C:\Users\Lenovo\Desktop\project"
data=os.listdir(path)
for x in data:
    temp=x[-1:-4:-1]
    if temp=="yp.":
        path=os.path.join(path, x)
        file=open(path,"r",encoding="utf-8")
        count=0
        for line in file:
            count+=1
        print(path,count)
        file.close()
# 1. 把文件夹路径存成一个变量（r"..." 那种写法），用它去拿文件名单
# 2. 遍历名单，判断是不是 .py 结尾 —— 这步你已经写好了，留着别动
# 3. 是 .py 的话：把「文件夹 + 文件名」拼成完整路径
#    （名单里只有名字，直接拿去 open 会找不到文件）
# 4. 用这个完整路径打开文件，一行一行数，把结果存进一个变量
# 5. 打印：文件名 + 行数
