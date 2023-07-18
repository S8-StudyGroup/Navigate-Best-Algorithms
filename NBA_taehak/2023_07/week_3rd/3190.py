# [BOJ] 3190. 뱀
# 소요 시간 : 00분
from collections import deque

size = int(input())
apple_cnt = int(input())
apple_rc = set()
for _ in range(apple_cnt):
    r, c = map(int, input().split())
    apple_rc.add((r-1, c-1))

L = int(input())                                            # L : snake 방향 변환 횟수
snake_info = deque([input().split() for _ in range(L)])     # snake_info = [(X, C), ...] : 게임 시작으로부터 X초 뒤에 C방향으로 회전 (C: L(왼), D(오른))

time = 0
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
di = 1
snake_rcs = deque([(0, 0)])

while True:
    time += 1

    # snake head
    hr, hc = snake_rcs[0]

    # 다음칸
    dr, dc = delta[di]
    nr = hr + dr
    nc = hc + dc

    # 게임 종료조건
    if (nr, nc) in snake_rcs or not (0 <= nr < size and 0 <= nc < size):
        break
    
    # snake head
    snake_rcs.appendleft((nr, nc))

    # 사과 먹는지
    if (nr, nc) in apple_rc:
        apple_rc.remove((nr, nc))
    else:
        snake_rcs.pop()

    # 방향 변환하는지
    if snake_info and int(snake_info[0][0]) == time:
        if snake_info[0][1] == 'L':
            di = (di - 1) % 4
        else:
            di = (di + 1) % 4
        snake_info.popleft()

    # print('===============================')
    # print('time :', time)
    # print('snake_rcs :', snake_rcs)
    # print('snake_info :', snake_info)
    # print('apple_rc :', apple_rc)

print(time)