import os
path=r"C:\Users\Lenovo\Desktop\project"
data=os.listdir(path)
for x in data:
    full = os.path.join(path, x)
    temp=x[-1:-4:-1]
    if temp=="yp.":
        file=open(full,"r",encoding="utf-8")
        count=0
        for line in file:
            count+=1
        print(x,count)
        file.close()
