#행렬값을 nm 숫자로 입력받는다
n, m = map(int, input().split())

x, y = 1, 1 #좌표 값을 0으로 초기화
arr = [[0 for _ in range(m)] for _ in range(n) ] # n곱하기 m행렬을 0으로 초기화

arr[x-1][y-1] = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_num = 0 # 0: 오른쪽, 1:아래, 2:왼쪽, 3:위

def in_range(x,y,n, m):
    return 0<x and x<=n and 0<y and y<=m

def can_go(x,y,n,m):
    return in_range(x,y,n,m) and arr[x-1][y-1]==0

num = 2
while num<=n*m:
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if not can_go(nx,ny,n,m):
        dir_num = (dir_num + 1) % 4

    x, y = x+dx[dir_num], y + dy[dir_num]

    arr[x-1][y-1]=num
    num +=1

for a in range(n):
    for b in range(m):
        print(arr[a][b], end = " ")
    print()