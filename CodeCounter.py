import os

path=r"C:\Users\Lenovo\Desktop\project"
data=os.listdir(path)
for x in data:
    full = os.path.join(path, x)
    temp=x[-1:-4:-1]
    if temp=="yp.":
        file=open(full,"r",encoding="utf-8")
        count_lines=0
        count_white_lines=0
        count_nomeaning_lines=0
        count_meaning_lines=0
        for line in file:
            count_lines+=1
            if line.strip()=="":
                count_white_lines+=1
            elif line.lstrip().startswith("#"):
                count_nomeaning_lines+=1
        count_meaning_lines=count_lines-count_white_lines-count_nomeaning_lines
        print(x,"总行数：",count_lines,",空行数：",count_white_lines,",注释行数：",count_nomeaning_lines,",代码行:",count_meaning_lines)
        file.close()

# 第 3 步：每个文件统计 总行数 / 代码行 / 空行 / 注释行
#
# 1. 前面拿名单、拼路径、判断 .py、打开文件 —— 全都不动
# 2. 原来只有一个 count，现在改成四个计数器，都从 0 开始
#    总行数、空行、注释行、代码行（名字自己取）
# 3. for line in file: 每读到一行：
#    - 总行数 +1
#    - 去掉首尾空白后是空的 → 空行 +1
#    - 否则，去掉左边空白后以 # 开头 → 注释行 +1
# 4. 循环结束后算代码行：总行数 − 空行 − 注释行
# 5. print 改成：文件名 + 这四个数