n = int(input())
d = 2

while d <= n:
    if n % d == 0:
        n /= d
        print(d)
    else:
        d += 1

