N = int(input())
S = [list(map(int,input().split(' '))) for i in range(N)]

def min_max(s):
    t = s[0]
    min, max = 0, 0
    if t == 1:
        min, max = s[1], s[2]
    elif t == 2:
        min, max = s[1], s[2]-0.01
    elif t == 3:
        min, max = s[1]+0.01, s[2]
    elif t == 4:
        min, max = s[1]+0.01, s[2]-0.01
    return min, max

def is_shared(s1, s2):
    min1, max1 = min_max(s1)
    min2, max2 = min_max(s2)
    r1 = (max1 >= min2) and (min1 < max2)
    r2 = (max1 > min2) and (min1 <= max2)
    r3 = (min1 < min2) and (max1 > max2)
    r4 = (min1 < min2) and (max1 > max2)
    return r1 or r2 or r3 or r4

c = 0
for i in range(1, N):
    for j in range(i+1, N+1):
        s1, s2 = S[i-1], S[j-1]
        if is_shared(s1, s2):
            c += 1

print(c)
