def is_prime(x):
    if x == 1:
        return False
    else:
        for i in range(2,int(x**0.5)+1):
            if x % i == 0:
                return False
        return True

a, b = map(int, input().split())

for i in range(a, b+1):
    if is_prime(i):
        print(i)