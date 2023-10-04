# [BOJ] 30036. INK
# 소요 시간 : 30분

from collections import deque
import sys
input = sys.stdin.readline

def jump(sy, sx, ink):
    if ink == 0: return
    
    queue = deque()
    queue.append((sy, sx, 0))
    visited = set()
    visited.add((sy, sx))

    while queue:
        y, x, cnt = queue.popleft()

        if stage[y][x] != ".":
            stage[y][x] = word[color]
        if cnt == ink:
            continue

        for dy, dx in move_command.values():
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in visited:
                visited.add((ny, nx))
                queue.append((ny, nx, cnt + 1))
                

I, N, K = map(int, input().split())
word = input()
ink = 0
color = 0
stage = []
ry, rx = 0, 0
move_command = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
    }

for i in range(N):
    row = list(input().rstrip())
    for j in range(N):
        if row[j] == "@":
            ry, rx = i, j
            row[j] = "."
    stage.append(row)

commands = input()
for command in commands:
    if command in move_command.keys():
        my, mx = ry + move_command[command][0], rx + move_command[command][1]
        if 0 <= my < N and 0 <= mx < N and stage[my][mx] == ".":
            ry, rx = my, mx

    elif command == "j":
        ink += 1

    elif command == "J":
        jump(ry, rx, ink)
        ink = 0
        color = (color + 1) % I

stage[ry][rx] = "@"
for i in range(N):
    print(*stage[i], sep="")