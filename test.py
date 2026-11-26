
for i in range(1,10):
    #外循环，从1-9
    for j in range(1,i+1):
        #内循环，从1-i
        print(f"{j}*{i}={j*i}\t",end="")
        #输出
    print()