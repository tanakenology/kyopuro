import sys

l = []
for i in sys.stdin:
    l.append(list(map(int,i.replace('\n','').split())))

p_list = l[1:]
A = 'Yes'

for i, p in enumerate(p_list):
    ti, xi, yi = p
    if i > 0:
        ti_1, xi_1, yi_1 = p_list[i-1]
    else:
        ti_1, xi_1, yi_1 = [0, 0, 0]
    a = (ti - ti_1) - (abs(xi_1-xi) + abs(yi_1-yi))
    if (a < 0) or ((a > 0) and (a % 2 == 1)):
        A = 'No'
        break

print(A)
