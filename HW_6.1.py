# 1.
n = 808
h = n//60
m = n % 60
h1 = h//10
h2 = h % 10
m1 = m//10
m2 = m % 10
sum_n = h1 + h2 + m1 + m2
print(sum_n)

# 2.
exp = 10
t_hold = 15
rew = 6
if exp + rew >= t_hold:
    print(True)
else:
    print(False)

# 3.
time_24 = "23:15"
h, m = map(int, time_24.split(":"))
if h < 12:
    day = "a.m."
    if h == 0:
        h = 12
else:
    day = "p.m."
    if h > 12:
        h -= 12
time_12 = f"{h}:{m:02d} {day}"
print(time_12)
