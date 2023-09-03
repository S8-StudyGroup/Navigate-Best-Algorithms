# [BOJ] 17822. 원판 돌리기
# 소요 시간 : 00분

from collections import deque
import sys
input = sys.stdin.readline
sum_boards = 0

N, M, T = map(int, input().split())
boards = [deque(map(int, input().split())) for _ in range(N)]
cnt_num = N * M

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for _ in range(T):
    x, d, k = map(int, input().split())
<<<<<<< HEAD
    mx = x
    while mx - 1 < len(boards):
        boards[mx - 1].rotate(k if d == 0 else -k)
        mx += x

    if cnt_num == 0: continue
    for dy, dx in direction:
        
=======
    for i in range(x - 1, N, x):
        boards[i].rotate(k if d == 0 else -k)

    check = False
    for i in range(N):
        for j in range(M):
            if boards[i][j] == 0: continue
            tmp = boards[i][j]
            for dy, dx in direction:
                ny, nx = i + dy, (j + dx) % M
                if 0 <= ny < N and boards[i][j] == boards[ny][nx]:
                    break
            else:
                continue

            check = True
            queue = deque()
            queue.append((i, j))
            
            while queue:
                y, x = queue.popleft()
                boards[y][x] = 0

                for dy, dx in direction:
                    ny, nx = y + dy, (x + dx) % M
                    if 0 <= ny < N and tmp == boards[ny][nx]:
                        queue.append((ny, nx))
    
    if not check:
        cnt, sum = 0, 0
        for i in range(N):
            for j in range(M):
                if boards[i][j] != 0:
                    cnt += 1
                    sum += boards[i][j]

        avg = sum / cnt

        for i in range(N):
            for j in range(M):
                if boards[i][j] != 0:
                    boards[i][j] += 1 if boards[i][j] < avg else -1

answer = 0
for i in range(N):
    for j in range(M):
        answer += boards[i][j]

print(answer)

# print(sum([sum(boards[i]) for i in range(N)]))
>>>>>>> a89be7563ab381919ea32c7c6d593956b0548cca
