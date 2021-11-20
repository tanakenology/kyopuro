import numpy as np

N = int(input())
s = [list(map(int,input().split(' '))) for i in range(N)]
populations = list(map(sum,s))

takahashi = 0
aoki = sum(np.array(s)[:,0])
sorted_indices = sorted(range(len(populations)), key=lambda k: populations[k], reverse=True)

ans = 0
for index in sorted_indices:
    ans += 1
    city = s[index]
    takahashi += populations[index]
    aoki -= city[0]
    if takahashi > aoki:
        break

print(ans)
