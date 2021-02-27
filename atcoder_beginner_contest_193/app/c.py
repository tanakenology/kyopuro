N = int(input())

if N < 4:
    print(N)
else:
    nums = []
    for a in range(2,int(N**(1/2))+1,1):
        b = 2
        while a**b <= N:
            nums.append(a**b)
            b += 1
    print(N-len(set(nums)))
