from datetime import datetime, timedelta

S, T, X = list(map(int,input().split(" ")))

if S > T:
    T += 24

now = datetime.now()
s_time = now + timedelta(hours=S)
t_time = now + timedelta(hours=T)
x_time = now + timedelta(hours=X, minutes=30)

if x_time >= s_time and x_time < t_time:
    print("Yes")
else:
    print("No")
