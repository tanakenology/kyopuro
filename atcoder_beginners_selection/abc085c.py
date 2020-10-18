n, y = list(map(int,input().split()))
A = None
flag = False

for i in range(n+1):
    for j in range(n+1-i):
        if 10000*i + 5000*j + 1000*(n-i-j) == y:
            print(i, j, n-i-j)
            flag = True
    if flag:
        break

if not flag:
    print(-1, -1, -1)
