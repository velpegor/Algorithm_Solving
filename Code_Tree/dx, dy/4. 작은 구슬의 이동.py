#첫 번째 줄에 격자의 크기를 나타내는 n과 시간 t를 입력받음
n, t = map(int,input().split())

#두 번째 줄에는 구슬의 정보(r행 c열 정보)와 바라보고 있는 방향 d를 입력받음
r, c, d = input().split()

dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]

#각 방향에 맞게 dx,dy의 인덱스 값을 배치해줌
mapper = {
    'R' : 0,
    'L' : 3,
    'U' : 1,
    'D' : 2
}
move_dir = mapper[d]
x, y = int(r), int(c)

def is_range(x, y, n):
    return 0<x and x<=n and 0<y and y<=n

for i in range(t):
    nx, ny = x + dx[move_dir], y + dy[move_dir]
    if is_range(nx,ny,n):
         x, y = nx, ny
    else:
        move_dir = 3 - move_dir

print(x, y)



