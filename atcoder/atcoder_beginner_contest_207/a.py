s = input()
A, B, C = list(map(int,s.split(' ')))
v1 = A + B
v2 = A + C
v3 = B + C
print(max([v1, v2, v3]))