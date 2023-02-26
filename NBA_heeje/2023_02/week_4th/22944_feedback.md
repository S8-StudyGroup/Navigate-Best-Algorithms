# [BOJ] 22944. 죽음의 비

### 🩹 **답변**

1. **개선 코드**
```python
from collections import deque

"""
조심할 점.
최단경로가 아니지만, 우산을 통해 도착하는 경우가 존재

방문지점을 현재 체력으로 저장... (아이디어가 중요하다..)
"""

def bfs():
    
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    que = deque()   
    # 0이 맨몸, 1이 우산
    visited = [[0] * N for _ in range(0, N)]

    flag = False
    for row in range(0, N):
        if flag:
            continue
        for col in range(0, N):
            if flag:
                continue
            if MAP[row][col] == "S":
                start_row = row
                start_col = col
                flag = True
    
    # 행, 열, 경로, 체력, 우산 (0이면 맨몸, 우산갖고있을 시, 우산 내구도)
    visited[row][col] = H
    que.append((start_row, start_col, 0, H, 0))
    
    while que:
        row, col, path, my_hp, umbrella_hp = que.popleft()

        if visited[row][col] and visited[row][col] > my_hp:
            continue

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue
            # 다음 지점이 안전지대
            if MAP[next_row][next_col] == SAFE_ZONE:
                return path+1
            if MAP[next_row][next_col] == UMBRELLA:
                next_umbrella_hp = D-1
                next_my_hp = my_hp
            else:
                if umbrella_hp > 0:
                    next_umbrella_hp = umbrella_hp-1
                    next_my_hp = my_hp
                else:
                    next_umbrella_hp = umbrella_hp
                    next_my_hp = my_hp-1
                if next_my_hp == 0:
                    continue
            # 방문을 이미 한 지역의 경우는 현재 저장된 값보다 큰 체력일때만 이동 가능
            if visited[next_row][next_col] and visited[next_row][next_col] >= next_my_hp:
                continue
            visited[next_row][next_col] = next_my_hp
            que.append((next_row, next_col, path+1, next_my_hp, next_umbrella_hp))   
    return -1


N, H, D = map(int, input().split())

UMBRELLA = "U"
SAFE_ZONE = "E"
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(input())

answer = bfs()
print(answer)
```

### 🌼 **도움되었던 내용**
chatGPT는 별 도움 안되서 정답자 중 실행 속도가 나와 5배 차이 나는 코드를 가져와보았다!