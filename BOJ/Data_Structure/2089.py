#다시 풀어볼것
n = int(input())
answer = ''

if n == 0:
    print('0')
    exit()

while n:
    if n % (-2) < 0:
        answer = '1' + answer
        n = n // - 2 + 1
    else:
        answer = '0' + answer
        n //= -2

print(answer)

