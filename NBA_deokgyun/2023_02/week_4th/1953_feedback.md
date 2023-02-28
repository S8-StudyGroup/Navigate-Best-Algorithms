# [SWEA] 1953. 탈주범 검거

### 🩹 **ChatGPT 답변**

1. **설명**

```plaintext
# ChatGPT의 코드 설명을 적어주세요.

코드를 보면 visited 리스트를 사용하여 방문 여부를 체크하고 있습니다. 그러나 visited 리스트는 cnt 값과 유사한 역할을 하고 있으므로 visited 리스트를 사용하는 대신, cnt 변수의 값을 이용하여 방문 여부를 체크하는 것이 코드를 간단하게 만들 수 있습니다.

또한, visited 리스트의 초기화를 하나의 루프에서 처리할 수 있습니다. 이를 위해서는, 큐에 삽입된 좌표를 visited 리스트에 기록하는 것이 아니라 큐에 삽입하기 전에 visited 리스트에 기록하면 됩니다. 이렇게 하면, 큐에서 좌표를 꺼낼 때마다 visited 리스트를 체크할 필요가 없으므로 코드가 간단해집니다.

```

2. **개선 코드**

```python
# ChatGPT의 개선된 코드를 적어주세요.

def bfs(start):
    queue = [start]
    cnt = 1
    visited = [[False] * M for _ in range(N)]
    visited[start[0]][start[1]] = True
    while queue:
        x, y = queue.pop(0)
        if cnt >= L:
            break
        for d in structure[tunnels[x][y]]:
            move_x, move_y = x + dx[d], y + dy[d]
            if (
                0 <= move_x < N
                and 0 <= move_y < M
                and tunnels[move_x][move_y] != 0
                and not visited[move_x][move_y]
                and (d + 2) % 4 in structure[tunnels[move_x][move_y]]
            ):
                visited[move_x][move_y] = True
                queue.append((move_x, move_y))
                cnt += 1
    return cnt


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

structure = {
    1: [0, 1, 2, 3],
    2: [0, 2],
    3: [1, 3],
    4: [0, 3],
    5: [2, 3],
    6: [1, 2],
    7: [0, 1],
}

T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnels = [list(map(int, input().split())) for _ in range(N)]

    print("#%d %d" % (tc, bfs((R, C))))

```

### 🌼 **도움되었던 내용**
