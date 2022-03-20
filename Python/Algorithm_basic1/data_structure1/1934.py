def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return(a*b // gcd(a, b))

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))