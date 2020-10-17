n, a, b = list(map(int,input().split()))
s = 0
for i in list(range(1,n+1)):
    l = [int(j) for j in list(str(i))]
    if (sum(l) >= a) and (sum(l) <= b):
        s += i
print(s)
