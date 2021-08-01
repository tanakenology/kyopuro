N, M = map(int,input().split()) 
A, B = [list(map(int, input().split())) for l in range(2)]

if max(A) <= min(B):
    print(abs(max(A) - min(B)))
elif min(A) >= max(B):
    print(abs(min(A) - max(B)))
elif max(A) >= max(B) and min(A) >= min(B):
    print(min(
        [abs(max(A) - max(B)), abs(min(A) - min(B))]
    ))
elif max(B) >= max(A) and min(B) >= min(A):
    print(min(
        [abs(max(A) - max(B)), abs(min(A) - min(B))]
    ))
else:
    A, B = sorted(A), sorted(B)
    
