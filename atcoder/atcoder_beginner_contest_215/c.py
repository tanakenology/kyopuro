from collections import Counter

s, k = input().split()
S, K = sorted(s), int(k)

c = Counter(S)
