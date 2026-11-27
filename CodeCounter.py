import os

path=r"C:\Users\Lenovo\Desktop\project"
data=os.listdir(path)
mydic={}
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
        mydic[x]=[count_lines,count_white_lines,count_nomeaning_lines,count_meaning_lines]
        file.close()

# 第 3.5 步：字典按扩展名累加 + 总计
#
# 1. 在 for x in data: 外面，先建一个空字典（比如 stats）
# 2. 判断 .py 成立、四个计数器都算完之后：
#    扩展名先直接写死 ".py"（现在只统计 py，下一步才放开别的扩展名）
# 3. 这个扩展名如果还不在字典里，先放一个全 0 的列表进去
#    列表装 5 个数：文件数、总行数、代码行、空行、注释行
#    （下标哪个对应哪个，自己写行注释记住，别到后面搞混）
# 4. 把本文件的四个计数器逐项加到列表对应位置，文件数 +1
# 5. for x 循环全部结束后：遍历字典，每个扩展名打一行汇总
# 6. 再打一行总计 = 字典里所有行对应位置相加
