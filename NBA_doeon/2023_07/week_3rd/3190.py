# [BOJ] 3190. 뱀
# 소요 시간 : 00분
'''
-1 : 벽
0 : 움직일 수 있는 다음 칸
2 : 사과
1 : 뱀이 차지한 공간

근데 뱀이 길어지기도 하니까 이동하기 전 위치도 계속 기억해야 하나
시간을 언제까지 계속 움직여야 하지?
시간 흐르는 걸 내가 계속 더해줘야 하나? 아님 다른 방법?
'''
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())

# 보드 만들고 벽은 -1로 색칠하기
board = [[0] * (n + 2) for _ in range(n + 2)]
for i in range(n + 2):
    for j in range(n + 2):
        if i == 0 or i == n + 1 or j == 0 or j == n + 1:
            board[i][j] = -1

# 보드에 사과 위치에 2로 색칠하기
k = int(input())
for _ in range(k):
    i, j = map(int, input().split())
    board[i][j] = 2

# 뱀의 이동경로 기록하기
play = []
l = int(input())
for _ in range(l):
    t, dir = input().split()
    play.append((int(t), dir))

board[1][1] = 1
dir = 0
now = 0 # 소요시간
snake = [(1, 1)]

while True:
    now += 1

    px, py = snake[-1]  # 현재 뱀 머리 위치
    nx, ny = px + dx[dir % 4], py + dy[dir % 4]   # 다음 뱀 머리 위치

    if board[nx][ny] == -1 or board[nx][ny] == 1:      # 벽이나 나 자신일 경우
        # now += 1
        break

    elif board[nx][ny] == 2:    # 사과 있는 곳
        snake.append((nx, ny))
        board[nx][ny] = 1
        # now += 1

    elif board[nx][ny] == 0:    # 사과 없는 곳
        snake.append((nx, ny))
        board[nx][ny] = 1
        tx, ty = snake.pop(0)
        board[tx][ty] = 0
        # now += 1

    if play and now == play[0][0]:   # 방향 전환 타이밍이면
        if play[0][1] == 'L':
            dir -= 1
        elif play[0][1] == 'D':
            dir += 1
        play.pop(0)

print(now)