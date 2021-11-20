s = input()
A, B = list(map(int,s.split(' ')))
ans = (A-B)/A*100
print(ans)