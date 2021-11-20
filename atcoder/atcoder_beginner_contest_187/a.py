a, b = list(map(int,input().split()))
s_a = sum(list(map(int,list(str(a)))))
s_b = sum(list(map(int,list(str(b)))))
print(max([s_a,s_b]))