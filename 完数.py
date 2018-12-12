#500以内完数(所有因子之和恰好等于本身，如6=1+2+3)
l = [ ]
for n in range(1,501):
    for a in range(1,n):
        if n%a == 0:
            l.append(a)
    if sum(l)==n:
        #print(l)
        print(n)
    l = []
