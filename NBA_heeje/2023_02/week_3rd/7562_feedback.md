# [BOJ] 7562. 나이트의 이동

### 🩹 **ChatGPT 답변**

1. **설명**
기존 코드에서 큰 개선사항은 없어보이지만, 몇 가지 작은 개선사항이 있습니다.

1. 리스트 컴프리헨션 사용하기

먼저, **`board`** 리스트를 초기화할 때 이중 for문을 사용하는 대신 리스트 컴프리헨션을 사용하면 더 간단하게 초기화할 수 있습니다.

```python
board = [[False] * l for _ in range(l)]
```

1. 불필요한 인덱스 계산 없애기

**`board`** 리스트를 사용하여 방문 여부를 체크할 때, 인덱스를 계산하는 부분이 여러번 반복됩니다. 이를 줄이기 위해 **`board`** 리스트의 인덱스를 직접 사용하는 것이 더 효율적입니다.

```python
if not board[move_y][move_x]:
    board[move_y][move_x] = True
    if (move_y, move_x) == goal:
        return cnt
    queue.append((move_y, move_x))
```

1. BFS 탐색하는 노드의 개수 구하기

BFS를 구현할 때, 탐색할 노드의 개수를 따로 구하고 있는데, 이를 **`queue`** 리스트의 길이를 이용해 간단하게 구할 수 있습니다.

```python
cnt = 0
while queue:
    cnt += 1
    for _ in range(len(queue)):
        y, x = queue.popleft()
        for d in range(8):
            move_y, move_x = y + dy[d], x + dx[d]
            if 0 <= move_y < l and 0 <= move_x < l and not board[move_y][move_x]:
                board[move_y][move_x] = True
                if (move_y, move_x) == goal:
                    return cnt
                queue.append((move_y, move_x))
```
2. **개선 코드**
```python
import sys
input = sys.stdin.readline
from collections import deque


dy = [1, 2, 1, 2, -1, -2, -1, -2]
dx = [2, 1, -2, -1, 2, 1, -2, -1]

def bfs(knight):
    board[knight[0]][knight[1]] = True
    queue = deque([knight])
    cnt = 0
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            y, x = queue.popleft()
            for d in range(8):
                move_y, move_x = y + dy[d], x + dx[d]
                if 0 <= move_y < l and 0 <= move_x < l and not board[move_y][move_x]:
                    board[move_y][move_x] = True
                    if (move_y, move_x) == goal:
                        return cnt
                    queue.append((move_y, move_x))
    
    return -1
    


T = int(input())

for _ in range(T):
    l = int(input())
    board = [[False] * l for _ in range(l)]
    knight = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))

    print(0 if knight == goal else bfs(knight))
```

### 🌼 **도움되었던 내용**
딱히 개선될 만한 내용은 없었다.