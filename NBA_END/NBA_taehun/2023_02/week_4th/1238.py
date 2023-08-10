# [SWEA] 1238. Contact
# 소요 시간 : 00분

from collections import deque

def bfs(num):
    visited = [False] * 101
    visited[num] = True
    v = [num, 1]
    queue = deque([v])
    result = {}
    while queue:
        num, cnt = queue.popleft()
        if cnt in result:
            result[cnt] += [num]
        else:
            result[cnt] = [num]
        for next_num in graph[num]:
            if not visited[next_num]:
                visited[next_num] = True
                queue.append([next_num, cnt + 1])
    return max(list(result.values())[-1])


for t in range(1, 11):
    n, sp = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for idx in range(0, n, 2):
        graph[arr[idx]].append(arr[idx + 1])
    print(f'#{t} {bfs(sp)}')
