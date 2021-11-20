N, X = input().split(" ")
leak_map = {str(i+1):v for i, v in enumerate(input().split(" "))}

friend = X
friends = set()
friends.add(friend)

for _ in range(int(N)):
    friend = leak_map[friend]
    friends.add(friend)

print(len(friends))
