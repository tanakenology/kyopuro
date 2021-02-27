N = int(input())
s = [list(map(int,input().split(' '))) for i in range(N)]

l = []

for a, p, x in s:
    if x - a > 0:
        l.append(p)

if len(l) > 0:
    print(min(l))
else:
    print(-1)
