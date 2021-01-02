import collections

N = int(input())
s = [input() for i in range(N)]

ans = 'satisfiable'

bikkuri = []
normal = []
for w in s:
    if w[0] == '!':
        bikkuri.append(w.lstrip('!'))
    else:
        normal.append(w)

bikkuri = list(set(bikkuri))
normal = list(set(normal))
d = dict(collections.Counter(bikkuri + normal))
fuman = list({k:v for k,v in d.items() if v > 1}.keys())

if len(fuman) > 0:
    ans = fuman[0]

print(ans)
