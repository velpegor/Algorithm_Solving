def count_num(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count

n, m = map(int, input().split())

five_count = count_num(n, 5) - count_num(m, 5) - count_num(n-m, 5)
two_count = count_num(n, 2) - count_num(m, 2) - count_num(n-m, 2)

answer = min(five_count, two_count)
print(answer)
