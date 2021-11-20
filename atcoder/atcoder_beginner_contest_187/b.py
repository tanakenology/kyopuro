import itertools

N = int(input())
s = [input() for i in range(N)]

count = 0
for v in itertools.combinations(s, 2):
    x1, y1 = list(map(int,v[0].split(' ')))
    x2, y2 = list(map(int,v[1].split(' ')))
    a = (y2 - y1)/(x2 - x1)
    if (a  >= -1) & (a <= 1):
        count += 1

print(count)
