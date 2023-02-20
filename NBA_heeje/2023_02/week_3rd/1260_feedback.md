# [BOJ] 1260. DFS와 BFS

### 🩹 **ChatGPT 답변**

1. **설명**
```plaintext
이 코드에서 개선할 점은 크게 두 가지입니다. 첫 번째는 입력 방식이고, 두 번째는 DFS와 BFS 함수의 구현 방식입니다.

입력 방식 개선:

현재 코드는 **`input`** 함수 대신 **`sys.stdin.readline`**을 사용하여 입력을 받습니다. 이 방법은 입력 속도를 높이기 위한 것이지만, 매번 **`strip()`** 함수를 사용해줘야 하기 때문에 코드가 지저분해집니다. 그리고 입력받은 값을 **`map`** 함수로 각각 int형으로 변환해줘야 하기 때문에 코드가 더 복잡해집니다. 이 문제를 해결하기 위해서는 **`input`** 함수를 그대로 사용하면 됩니다.

DFS와 BFS 함수 구현 방식 개선:

현재 코드에서는 DFS와 BFS 함수의 구현 방식이 거의 동일합니다. 이를 개선하기 위해서는 DFS와 BFS 함수에서 수행하는 작업이 거의 같으므로, 공통된 작업을 함수로 따로 분리해주는 것이 좋습니다. 또한, DFS와 BFS 함수에서 방문 여부를 체크하는 **`visited`** 리스트를 매번 초기화해주는 것이 번거로우므로, 초기화 작업을 하나의 함수로 분리해주는 것이 좋습니다.
```
2. **개선 코드**
```python
import sys

def dfs(v):
    visited[v] = True
    dfs_list.append(v)
    for w in sorted(adj_list[v]):
        if not visited[w]:
            dfs(w)

def bfs(v):
    visited[v] = True
    queue = [v]
    while queue:
        v = queue.pop(0)
        bfs_list.append(v)
        for w in sorted(adj_list[v]):
            if not visited[w]:
                visited[w] = True
                queue.append(w)

def reset_visited():
    for i in range(1, N+1):
        visited[i] = False

input = sys.stdin.readline
N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

dfs_list = []
bfs_list = []

dfs(V)
reset_visited()
bfs(V)

print(*dfs_list)
print(*bfs_list)
```

### 🌼 **도움되었던 내용**
초기화 작업을 하나의 함수로 분리해주는 것이 더 깔끔하다고 생각했다.