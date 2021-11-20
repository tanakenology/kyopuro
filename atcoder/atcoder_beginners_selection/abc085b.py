import sys

l = []
for i in sys.stdin:
    l.append(int(i))

d_list = l[1:]

print(len(set(d_list)))
