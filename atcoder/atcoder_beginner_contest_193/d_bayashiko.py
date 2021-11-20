from collections import defaultdict

K = int(input())
S = input()
S_counter = defaultdict(int)
for i in range(0, 4):
    S_counter[int(S[i])] += 1

T = input()
T_counter = defaultdict(int)
for i in range(0, 4):
    T_counter[int(T[i])] += 1

totalCards = 9 * K
probabilities_S = {}

for num in range(1, 10):
    alreadyExists = S_counter[num] + T_counter[num]
    rest = K - alreadyExists
    probability = rest / (totalCards - 8)
    probabilities_S[num] = probability

def calcScore(cards):
    output = 0
    for i in range(1, 10):
        output += i * 10 ** cards[i]
    return output

scoreDict_S, scoreDict_T = defaultdict(float), defaultdict(float)


restCards = {}
for i in range(1, 10):
    rest = K - S_counter[i] - T_counter[i]
    restCards[i] = rest

def isValid(i, j):
    if i == j:
        return 2 <= restCards[i]
    else:
        return restCards[i] >= 1 and restCards[j] >= 1

#残りのカードから、(i, j)を取り出す確率
def prob(i, j):
    restTotal = totalCards - 8 #残りの枚数
    totalPattern = restTotal * (restTotal - 1) #残りカードから2枚取るパターン
    if i == j:
        rest_i = restCards[i]
        pattern = rest_i * (rest_i - 1)
    else:
        rest_i, rest_j = restCards[i], restCards[j]
        pattern = rest_i * rest_j

    probability = pattern / totalPattern
    return probability

output = 0
for i in range(1, 10):
    for j in range(1, 10):
        if isValid(i, j):
            S_counter[i] += 1
            T_counter[j] += 1
            score_S, score_T = calcScore(S_counter), calcScore(T_counter)
            S_counter[i] -= 1
            T_counter[j] -= 1

            if score_S > score_T:
                output += prob(i, j)

print(output)
