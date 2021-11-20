s = input()
A, B = list(map(int,s.split(' ')))

ans = ''
if A > 0 and B == 0:
    ans = 'Gold'
elif A == 0 and B > 0:
    ans = 'Silver'
else:
    ans = 'Alloy'

print(ans)
