s = input()
A, B, C, D = list(map(int,s.split(' ')))

class Bowl:
    def __init__(self, blue, red):
        self.blue = blue
        self.red = red
        self.all = blue + red

    def add(self, blue_add, red_add):
        self.blue += blue_add
        self.red += red_add
        self.all = self.blue + self.red

    def judge(self, d):
        return self.blue <= self.red * d

bowl = Bowl(A, 0)

if B >= C * D:
    ans = -1
else:
    ans = 0
    while True:
        if bowl.judge(D):
            break
        else:
            bowl.add(B, C)
            ans += 1

print(ans)
