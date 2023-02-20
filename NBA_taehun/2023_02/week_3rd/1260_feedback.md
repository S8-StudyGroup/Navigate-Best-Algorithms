# [BOJ] 1260. DFS와 BFS

### 🩹 **ChatGPT 답변**

1. **설명**

```plaintext
# ChatGPT의 코드 설명을 적어주세요.
1. from collections import deque 를 코드 상단에 import 문으로 옮겨왔습니다.
2. map(int, input().strip().split()) 을 map(int, input().split()) 으로 변경하여 줄임표를 사용하지 않았습니다.
3. visited 리스트 초기값을 [True] + [False] * N 에서 [False] * (N + 1) 로 변경하였습니다.
4. 리스트 컴프리헨션을 사용하여 graph 리스트를 초기화할 때, graph = [sorted(adj_list) for adj_list in graph] 로 변경하였습니다. 이는 모든 인접 리스트를 정렬하여 출력 결과가 일정하게 유지될 수 있도록 합니다.
```

2. **개선 코드**

```python
# ChatGPT의 개선된 코드를 적어주세요.
import sys
from collections import deque

input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    result.append(v)
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)

def bfs(v):
    visited = [True] + [False] * N
    dq = deque([v])
    visited[v] = True
    while dq:
        v = dq.popleft()
        result.append(v)
        for next_v in graph[v]:
            if not visited[next_v]:
                dq.append(next_v)
                visited[next_v] = True

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

graph = [sorted(adj_list) for adj_list in graph]

visited = [False] * (N + 1)
result = []
dfs(V)
print(*result)

result = []
bfs(V)
print(*result)
```

### 🌼 **도움되었던 내용**

visited의 리스트 초기값을 [False] \* (N + 1)으로 설정한 것
