# [BOJ] 9019. DSLR
# 소요 시간 : 00분

from collections import deque

calcul = {
    "D":lambda x: (2*x)%10000,
    "S":lambda x: x-1 if x > 0 else 9999,
    "L":lambda x: (x % 1000)*10 + x // 1000,
    "R":lambda x: (x%10) * 1000 + x // 10
}

for _ in range(int(input())):
    start, target = map(int, input().split())
    visited = [False for _ in range(10000)]

    queue = deque([[start, ""]])
    visited[start] = True

    while queue:
        now, step = queue.popleft()
        
        if now == target:
            print(step)
            break

        dnum = calcul["D"](now)
        snum = calcul["S"](now)
        lnum = calcul["L"](now)
        rnum = calcul["R"](now)

        if not visited[dnum]:
            visited[dnum] = True
            queue.append([dnum, step+"D"])
        if not visited[snum]:
            visited[snum] = True
            queue.append([snum, step+"S"])
        if not visited[lnum]:
            visited[lnum] = True
            queue.append([lnum, step+"L"])
        if not visited[rnum]:
            visited[rnum] = True
            queue.append([rnum, step+"R"])