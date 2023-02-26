# [SWEA] 1953. 탈주범 검거

### 🩹 **ChatGPT 답변**

1. **설명**
```plaintext
코드가 체계적이고 잘 작성되었습니다. 그러나 다음은 개선을 위한 몇 가지 사소한 제안입니다.

빈 집합에 대해 set([]) 대신 set()를 사용하십시오. 예를 들어 visited = set([]) 대신 visited = set()라고 간단히 작성할 수 있습니다.
코드에서 불필요한 공백을 피하십시오. . 예를 들어, visited 대신. add((R, C)), visited.add((R, C))를 작성할 수 있습니다.
문자열 서식 지정을 위해 f-문자열을 사용합니다. "#" + str(tc) + " " + str(len(visited)) 대신 f"#{tc} {len(visited)}".
bfs() 함수에 docstring을 추가하여 용도와 매개변수를 설명합니다.
코드에 주석을 추가하여 특히 tunnel_info 목록의 경우 각 부분이 그렇습니다.
```
2. **개선 코드**
```python
from collections import deque


def bfs():
    """
    Perform a breadth-first search to find all reachable locations from the starting point (R, C) within L time steps.
    :return: A string containing the number of reachable locations
    """
    visited = set()
    visited.add((R, C))
    queue = deque()
    queue.append((R, C, 1))

    while queue:
        y, x, time = queue.popleft()

        if time == L:
            break

        for d in tunnel_info[matrix[y][x]]:
            move_y, move_x = y + dy[d], x + dx[d]

            if (0 <= move_y < N and 0 <= move_x < M and
                (move_y, move_x) not in visited and
                (d + 2) % 4 in tunnel_info[matrix[move_y][move_x]]):
                visited.add((move_y, move_x))
                queue.append((move_y, move_x, time + 1))

    return f"#{tc} {len(visited)}"


# Search up and down
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

# Whether or not each tunnel is connected in each direction [top, left, bottom, right]
tunnel_info = [
    [],
    [0, 1, 2, 3],
    [0, 2],
    [1, 3],
    [0, 3],
    [2, 3],
    [1, 2],
    [0, 1],
]

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    print(bfs())
```

### 🌼 **도움되었던 내용**
딱히 도움될 만한 내용은 없었다.
다만 if문이 길어질 때 괄호 쓰면 좋다는 거 말씀드리기