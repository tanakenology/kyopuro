S = input()

d = {}
for c in ['c', 'h', 'o', 'k', 'u', 'd', 'a', 'i']:
    d[c] = [n for n, v in enumerate(list(S)) if v == c]

def calc(d):
    for c in ['c', 'h', 'o', 'k', 'u', 'd', 'a', 'i']:
        if len(d[c]) == 0:
            return 0

    min_num = {}
    for c in ['c', 'h', 'o', 'k', 'u', 'd', 'a', 'i']:
        min_num[c] = min(d[c])

    if sorted(min_num.values()) != list(min_num.values()):
        return 0

    count = 0
    for ci in d['c']:
        for hi in d['h']:
            for oi in d['o']:
                for ki in d['k']:
                    for ui in d['u']:
                        for di in d['d']:
                            for ai in d['a']:
                                for ii in d['i']:
                                    l = [ci, hi, oi, ki, ui, di, ai, ii]
                                    if sorted(l) == l:
                                        count += 1

    return count % (1000000000 + 7)

print(calc(d))
