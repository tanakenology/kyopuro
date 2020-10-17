s = input()

l = s.replace('d','-d').replace('era','-era').split('-')[1:]
l = list(set(l))
l = [e for e in l if e not in ['dream','dreamer','erase','eraser']]

if len(l) == 0:
    print('YES')
else:
    print('NO')
