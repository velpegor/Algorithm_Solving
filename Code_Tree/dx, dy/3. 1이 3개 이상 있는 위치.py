#n을 입력받음. n은 n개의 줄을 의미
n = int(input())

# 배열을 입력받아서 list에 저장
arr = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

#x, y가 배열의 범위내에 있는지를 확인하는 함수
def is_range(x, y, n):
    return 0<=x and x<n and 0<=y and y<n

#x, y좌표에서 상하좌우에 1이 몇 개 있는지 세는 함수
def adjacent_cnt(x, y):
    cnt = 0
    for i, j in zip(dx, dy):
        nx, ny = x + i, y + j
        if is_range(nx, ny, n) and arr[nx][ny] == 1:
            cnt +=1
    return cnt

count = 0
for i in range(n):
    for j in range(n):
        if adjacent_cnt(i,j) >=3:
            count +=1

print(count)