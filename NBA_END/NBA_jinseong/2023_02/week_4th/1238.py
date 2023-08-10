# [SWEA] 1238. Contact
# 소요 시간 : 60분

def contact(v):
    visited = [False] * 101
    visited[v] = True
    # [몇번만에, 연락된 사람, ....]
    last = [-1, 0]

    queue = [[0, v]]
    while queue:
        now_depth, now_v = queue.pop(0)
        if now_depth > last[0]:
            last = [now_depth, now_v]
        else:
            last.append(now_v)
        if now_v in info.keys():
            for next_v in info[now_v]:
                if not visited[next_v]:
                    visited[next_v] = True
                    queue.append([now_depth + 1, next_v])
    return max(last[1:])


for t in range(1, 11):
    n, start = map(int, input().split())
    data = list(map(int, input().split()))

    # info : [[from, to, to, ...], ...]
    info = {}
    # match : 현재사람 -> visited index
    match = {}
    for i in range(n // 2):
        r = 2 * i
        if data[r] in info.keys():
            info[data[r]].append(data[r + 1])
        else:
            info[data[r]] = [data[r + 1]]

    ans = contact(start)

    print(f'#{t} {ans}')