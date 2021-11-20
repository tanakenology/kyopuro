N = int(input())
s = [list(map(int,input().split(' '))) for i in range(N)]

class Bag:
    def __init__(self):
        self.content = []
        self.min_list = []

    def op(self, i, x=None):
        if i == 1:
            self.content.append(x)
        elif i == 2:
            self.content = list(map(lambda n: n + x, self.content))
        elif i == 3:
            v = min(self.content)
            self.min_list.append(v)
            self.content.remove(v)

bag = Bag()
for q in s:
    if q[0] == 3:
        bag.op(q[0])
    else:
        bag.op(q[0], q[1])

print('\n'.join(list(map(str,bag.min_list))))
