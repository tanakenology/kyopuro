S = [input() for i in range(4)]

ans = 'No'
if ('H' in S) and ('2B' in S) and ('3B' in S) and ('HR' in S):
    ans = 'Yes'

print(ans)
