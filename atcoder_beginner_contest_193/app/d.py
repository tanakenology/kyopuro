import itertools

N = 3
K, S, T = [input() for i in range(N)]

all_cards = list(range(1,10)) * int(K)
s_cards = list(map(int,list(S[:-1])))
t_cards = list(map(int,list(T[:-1])))

print(all_cards)
print(s_cards)
print(t_cards)

for n in s_cards + t_cards:
    all_cards.remove(n)
sharp_nums = sorted(all_cards)

print(sharp_nums)

perms = list(itertools.permutations(sharp_nums, 2))
s_wins = 0
for s, t in perms:
    s_score = 0
    t_score = 0
    for i in range(1, 10):
        s_score += i * 10**((s_cards+[s]).count(i))
        t_score += i * 10**((t_cards+[t]).count(i))
    if s_score > t_score:
        s_wins += 1

print(s_wins/len(perms))
