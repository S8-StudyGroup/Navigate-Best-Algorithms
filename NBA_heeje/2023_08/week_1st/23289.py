# [BOJ] 23289. 온풍기 안녕!
# 소요 시간 : 00분

from collections import deque
import sys
input = sys.stdin.readline


def is_wall(x, y, d, heat_d):
    if heat_d == 1:
        if d == 0 and ((x, y, 0) in walls or (x - 1, y, 1) in walls):
            return True
        elif d == 1 and (x, y, 1) in walls:
            return True
        elif d == 2 and ((x + 1, y, 0) in walls or (x + 1, y, 1) in walls):
            return True
    elif heat_d == 2:
        if d == 0 and ((x - 1, y - 1, 1) in walls or (x, y, 0) in walls):
            return True
        elif d == 1 and (x, y - 1, 1) in walls:
            return True
        elif d == 2 and ((x + 1, y - 1, 0) in walls or (x + 1, y - 1, 1) in walls):
            return True
    elif heat_d == 3:
        if d == 0 and ((x, y - 1, 0) in walls or (x, y - 1, 1) in walls):
            return True
        elif d == 1 and (x, y, 0) in walls:
            return True
        elif d == 2 and ((x, y + 1, 0) in walls or (x, y, 1) in walls):
            return True
    else:
        if d == 0 and ((x + 1, y - 1, 0) in walls or (x, y - 1, 1) in walls):
            return True
        elif d == 1 and (x + 1, y, 0) in walls:
            return True
        elif d == 2 and ((x + 1, y + 1, 0) in walls or (x, y, 1) in walls):
            return True

    return False

def make_wind():
    winds = [[0] * C for _ in range(R)]
    for x, y, heat_d in heaters:
        hx, hy = x + dx[heat_d], y + dy[heat_d]
        winds[hx][hy] += 5
        queue = deque()
        queue.append((hx, hy, 5))
        visited = set()

        for _ in range(4):
            for _ in range(len(queue)):
                x, y, cnt = queue.popleft()
                for d in range(3):
                    nx, ny = x + wind_dx[heat_d][d], y + wind_dy[heat_d][d]
                    if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in visited and not is_wall(x, y, d, heat_d):
                        winds[nx][ny] += cnt - 1
                        visited.add((nx, ny))
                        queue.append((nx, ny, cnt - 1))
    
    for i in range(R):
        for j in range(C):
            room[i][j] += winds[i][j]


def control_temperature():
    temps = [[0] * C for _ in range(R)]
    visited = [[False] * C for _ in range(R)]
    
    for x in range(R):
        for y in range(C):
            visited[x][y] = True
            total = 0
            for d in range(1, 5):
                nx, ny = x + dx[d], y + dy[d]
                if nx < 0 or nx >= R or ny < 0 or ny >= C or visited[nx][ny]: continue
                if d == 1 and (x, y, 1) in walls: continue
                elif d == 2 and (x, y - 1, 1) in walls: continue
                elif d == 3 and (x, y, 0) in walls: continue
                elif d == 4 and (x + 1, y, 0) in walls: continue

                diff = int((room[x][y] - room[nx][ny]) / 4)
                total -= diff
                temps[nx][ny] += diff
            
            temps[x][y] += total
    
    for i in range(R):
        for j in range(C):
            room[i][j] += temps[i][j]


def decrease_temperature():
    for i in range(R):
        for j in range(C):
            if (i == 0 or i == R - 1 or j == 0 or j == C - 1) and room[i][j] != 0:
                room[i][j] -= 1
                


R, C, K = map(int, input().split())
room = []
heaters = []
checkpoints = []
walls = set()
chocolates = 0

for i in range(R):
    row = list(map(int, input().split()))
    for j in range(C):
        if 1 <= row[j] <= 5:
            if row[j] == 5:
                checkpoints.append((i, j))
            else:
                heaters.append((i, j, row[j]))
            row[j] = 0
    room.append(row)

W = int(input())
for _ in range(W):
    x, y, t = map(int, input().split())
    walls.add((x - 1, y - 1, t))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

wind_dx = [(), (-1, 0, 1), (-1, 0, 1), (-1, -1, -1), (1, 1, 1)]
wind_dy = [(), (1, 1, 1), (-1, -1, -1), (-1, 0, 1), (-1, 0, 1)]
for i in range(100):

# 1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴
    make_wind()
# 2. 온도가 조절됨
    control_temperature()
# 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
    decrease_temperature()
# 4. 초콜릿 냠
    chocolates += 1
# 조사하려는 모든 칸의 온도가 K 이상이면 테스트 종료
    for x, y in checkpoints:
        if room[x][y] < K: break
    else:
        print(chocolates)
        break
else:
    print(101)