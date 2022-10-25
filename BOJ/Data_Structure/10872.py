def fact(n):
    num = 1
    if n > 0:
        num = n * fact(n-1)
    return num

n = int(input())
print(fact(n))
