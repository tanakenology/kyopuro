s = input()
X1, X2, X3, X4 = list(map(int,list(s)))

ans = 'Strong'

def add(n):
    if n == 9:
        return 0
    else:
        return n + 1

req1 = X1 == X2 == X3 == X4
req2 = X4 == add(X3) == add(add(X2)) == add(add(add(X1)))

if req1 or req2:
    print('Weak')
else:
    print('Strong')
