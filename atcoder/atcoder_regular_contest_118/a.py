import math

s = input()
t, N = list(map(int,s.split(' ')))

def tax_included_price(a):
    v = (100 + t) / 100 * a
    return math.floor(v)

before_num = 1
current_num = 2
before_price = 1
current_price = 2
i = 1
ans = 0

while True:
    before_price = tax_included_price(before_num)
    current_price = tax_included_price(current_num)
    if (current_price - before_price) > 1:
        price = before_price+1
        i += 1
        if i == N+1:
            ans = price
            break
    before_num += 1
    current_num += 1

print(ans)
