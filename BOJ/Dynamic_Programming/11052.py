n = int(input())
d = [0] * (n+1) # n개의 최대값을 저장하는 배열 / 카드 i개 구매하는 최대가격
card_price = [0] + list(map(int, input().split())) # k개가 들어있는 카드팩의 가격
d[1] = card_price[1]
d[2] = max(card_price[2], card_price[1] * 2)

for i in range(3, n+1):
    d[i] = card_price[i]
    for j in range(1, i+1):
        d[i] = max(d[i], d[i-j] + d[j])

print(max(d))
