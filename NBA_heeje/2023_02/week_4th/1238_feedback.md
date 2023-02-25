# [SWEA] 1238. Contact

### 🩹 **ChatGPT 답변**

1. **설명**
```plaintext
귀하의 코드는 이미 잘 작성되어 있고 주어진 문제에 대해 효율적입니다. 그러나 약간의 최적화 및 개선이 가능합니다.

1. 중복 항목을 제거하려면 목록 대신 집합을 사용하십시오.
정점이 이미 인접 목록에 있는지 확인할 때 **`not in`** 연산자를 사용하여 목록을 검색합니다. 이는 각 요소를 하나씩 확인해야 하기 때문에 큰 목록에는 비효율적입니다. 목록 대신 집합을 사용하여 인접 목록을 저장하고 **`add`** 메서드를 사용하여 새 요소를 추가할 수 있습니다. 이렇게 하면 자동으로 중복 항목이 제거되고 성능이 향상됩니다.
2. 변수를 사용하여 최대 연락처 수를 저장하십시오.
**`bfs`** 함수에서 연락처 수가 가장 많은 사람을 검색하는 대신 변수를 사용하여 지금까지 본 최대 연락처 수를 저장하고 방문한 목록을 순회하면서 업데이트할 수 있습니다. 이렇게 하면 추가 루프가 필요하지 않고 성능이 향상됩니다.
```
2. **개선 코드**
```python
from collections import deque

def bfs(start):
    visited = [0] * 101
    visited[start] = 1
    queue = deque()
    queue.append((start, 1))
    max_contacts = 1

    while queue:
        v, cnt_contact = queue.popleft()
        for w in adj_list[v]:
            if visited[w] == 0:
                visited[w] = cnt_contact + 1
                queue.append((w, cnt_contact + 1))
                max_contacts = max(max_contacts, cnt_contact + 1)

    ans = max(range(1, 101), key=lambda x: (visited[x], -x))
    return ans

for tc in range(1, 11):
    length_of_data_list, start = map(int, input().split())
    data_list = list(map(int, input().split()))
    adj_list = [set() for _ in range(101)]

    for i in range(0, length_of_data_list, 2):
        adj_list[data_list[i]].add(data_list[i + 1])

    print(f"#{tc} {bfs(start)}")
```

### 🌼 **도움되었던 내용**
`adj_list = [set() for _ in range(101)]` 중복제거할 때 내 방법보다 chatGPT가 추천해 준 방식이 더 효율적이다!