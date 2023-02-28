# [SWEA] 1238. Contact
# 소요 시간 : 00분
from collections import deque


def bfs(start):
    visited = [False] * 101
    depth = [0] * 101
    q = deque([start])

    visited[start] = True

    while q:
        contact = q.popleft()
        for next_contact in graph[contact]:
            if not visited[next_contact]:
                visited[next_contact] = True
                depth[next_contact] = depth[contact] + 1
                q.append(next_contact)

    number, max_depth = 0, 0
    for i in range(101):
        if depth[i] >= max_depth:
            max_depth = depth[i]
            number = i

    return number


for case in range(1, 11):
    edge_len, start = map(int, input().split())
    edge_info = deque(map(int, input().split()))

    edges = set()
    for _ in range(edge_len//2):
        edges.add((edge_info.popleft(), edge_info.popleft()))
    edges = list(edges)

    graph = [[]for _ in range(101)]
    for i in edges:
        from_, to_ = i
        graph[from_].append(to_)

    print(f'#{case} {bfs(start)}')