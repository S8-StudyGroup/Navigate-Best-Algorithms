# [SWEA] 1238. Contact
# 소요 시간 : 00분

from collections import deque

for tc in range(10):
    l, start = map(int, input().split())
    data = list(map(int, input().split()))

    to = [[] for _ in range(101)]
    visited = [0] * 101

    for i in range(l // 2):
        to[data[i * 2]].append(data[i * 2 + 1])

    que = deque()
    que.append([start, 1])
    visited[start] = 1

    result = 0
    max_step = 0

    while que:
        num, step = que.popleft()
        if max_step < step:
            max_step = step
            result = num
        if max_step == step and result < num:
            result = num

        for n in to[num]:
            if not visited[n]:
                que.append([n, step + 1])
                visited[n] = 1

    print(f'#{tc + 1} {result}')