# [BOJ] 7562. 나이트의 이동

### 🩹 **ChatGPT 답변**

1. **설명**

```plaintext
# ChatGPT의 코드 설명을 적어주세요.
함수 인자로 시작점과 끝점 좌표를 tuple로 전달받도록 변경
이동 가능한 방향 탐색 방식을 변경하여 사분면 별로 분리하지 않고 8방향을 모두 탐색하도록 변경
좌표 인덱스를 1부터 시작하도록 변경 (기존 코드에서는 0부터 시작)
전역 변수 사용을 최소화하도록 변경 (함수 내에서 필요한 변수들을 모두 지역 변수로 선언)
```

2. **개선 코드**

```python
# ChatGPT의 개선된 코드를 적어주세요.
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, end, n):
    # 방문 처리
    visited = set()

    # deque 선언
    dq = deque([(*start, 0)])
    visited.add(start)

    # 목표 위치에 도착한 경우
    if start == end:
        return 0

    while dq:
        r, c, cnt = dq.popleft()

        # 이동 가능한 방향 탐색
        directions = []
        if r > 1:
            if c > 2:
                directions.append((-2, -1))
            if c < n - 1:
                directions.append((-2, 1))
        if r > 2:
            if c > 1:
                directions.append((-1, -2))
            if c < n:
                directions.append((-1, 2))
        if r < n - 1:
            if c > 2:
                directions.append((2, -1))
            if c < n - 1:
                directions.append((2, 1))
        if r < n:
            if c > 1:
                directions.append((1, -2))
            if c < n - 1:
                directions.append((1, 2))

        # 다음 위치를 탐색하며 deque에 추가
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # 이동할 위치가 목표 위치인 경우
            if (nr, nc) == end:
                return cnt + 1

            # 다음 위치가 범위 내에 있고, 방문하지 않은 곳일 때
            if 1 <= nr <= n and 1 <= nc <= n and (nr, nc) not in visited:
                visited.add((nr, nc))
                dq.append((nr, nc, cnt + 1))

    return -1

# 테스트 케이스
tc = int(input().strip())
result = []
for _ in range(tc):
    n = int(input().strip())
    start = tuple(map(int, input().strip().split()))
    end = tuple(map(int, input().strip().split()))

    # bfs
    result.append(bfs(start, end, n))

print(*result, sep='\n')
```

### 🌼 **도움되었던 내용**

시작 위치와 끝 위치를 start와 end라는 튜플의 형태로 변수에 저장해 함수의 파라미터로 전달한 것이 좋았습니다.
