# [BOJ] 15971. 두 로봇
# 소요 시간 : 10분

from collections import deque
import sys
input = sys.stdin.readline


def bfs(n1, n2):
    visited = set()
    queue = deque()
    queue.append((n1, 0, 0))
    visited.add(n1)

    while queue:
        n, max_dist, sum_dist = queue.popleft()

        if n == n2:
            return sum_dist - max_dist

        for v, dist in adj_list[n]:
            if v not in visited:
                visited.add(v)
                queue.append((v, max(max_dist, dist), sum_dist + dist))


N, R1, R2 = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    n1, n2, dist = map(int, input().split())
    adj_list[n1].append((n2, dist))
    adj_list[n2].append((n1, dist))

print(bfs(R1, R2))