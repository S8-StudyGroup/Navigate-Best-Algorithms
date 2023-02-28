# [SWEA] 1238. Contact

### 🩹 **ChatGPT 답변**

1. **설명**

```plaintext
# ChatGPT의 코드 설명을 적어주세요.
```

2. **개선 코드**

```python
# ChatGPT의 개선된 코드를 적어주세요.
from collections import deque

for test_count in range(1, 11):
    # Read input
    line_count, starting_person = map(int, input().split())
    lines = {}
    for _ in range(line_count):
        stations = list(map(int, input().split()))[1:]
        for i in range(1, len(stations)):
            line = stations[i-1]
            station = stations[i]
            if line not in lines:
                lines[line] = []
            lines[line].append(station)

    # Compute distances
    distance_list = [0] * 101
    distance = 1
    queue = deque([starting_person])
    while queue:
        i = queue.popleft()
        for k in lines.get(i, []):
            if distance_list[k] == 0:
                queue.append(k)
                distance_list[k] = distance_list[i] + 1
        distance += 1

    # Find last person
    max_distance = max(distance_list)
    last_people_list = [p for p in range(1, 101) if distance_list[p] == max_distance]
    last_person = max(last_people_list)

    # Print output
    print(f"#{test_count} {last_person}")
```

### 🌼 **도움되었던 내용**

chatGPT가 짜준 코드는 메모리 에러가 납니다…
