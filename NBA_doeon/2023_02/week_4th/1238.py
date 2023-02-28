# [SWEA] 1238. Contact
# 소요 시간 : 30분

def bfs(v):
    queue = []
    queue.append(v)
    visited[v] = 1

    while queue:
        p = queue.pop(0)
        if p in link:
            for next in link[p]:
                if visited[next] == 0:
                    queue.append(next)
                    visited[next] = visited[p] + 1


for tc in range(1, 11):
    length, start = map(int, input().split())
    arr = list(map(int, input().split()))
    link = dict()

    for idx in range(0, length, 2):
        s, e = arr[idx], arr[idx + 1]

        if s in link:
            link[s].append(e)
        else:
            link[s] = [e]

    visited = [0] * (101)

    bfs(start)

    last_num = 0
    last_idx = -1

    for idx, value in enumerate(visited):
        if value >= last_num:
            last_num = value
            last_idx = idx

    print(f'#{tc} {last_idx}')