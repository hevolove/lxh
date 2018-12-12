#500以内盈数(一个正整数除了本身之外所有因子之和大于本身，如12<1+2+3+4+6)
l = [ ]
for n in range(1,501):
    for a in range(1,n):
        if n%a == 0:
            l.append(a)
    if sum(l)>n:    #因子之和大于n本身
        #print(l)
        print(n)
    l = []
