a = [int(input()) for i in range(4)]
d = {500:a[0],100:a[1],50:a[2]}
s = []

for c500 in [500*i for i in range(d[500]+1)]:
    for c100 in [100*i for i in range(d[100]+1)]:
        for c50 in [50*i for i in range(d[50]+1)]:
            s.append(c500+c100+c50)

print(s.count(a[3]))
