l = [input().split() for l in range(2)]
n = int(l[0][0])
a_list = sorted([int(i) for i in l[1]],reverse=True)

alice_sum = 0
bob_sum = 0

for j,a in enumerate(a_list):
    if j % 2 == 0:
        alice_sum += a
    else:
        bob_sum += a

print(alice_sum - bob_sum)
