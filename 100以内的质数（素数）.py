import math
l = [ ]
for a in range(1,100):
    for b in range(2,int(math.sqrt(a)+1)):#质数只需要不能整除2~根号自己就可以了。
        l.append(a%b)  #将所有b遍历的结果加到列表中
    if 0 not in l:
        print(a,' ',end='')
    l = [ ] #执行完一次b的遍历将列表清空。
