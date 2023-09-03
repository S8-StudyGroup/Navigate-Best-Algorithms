# [BOJ] 17822. 원판 돌리기
# 소요 시간 : 00분

from collections import deque

insp = lambda : list(map(int, input().split()))

n,m,t = insp()

wonpan = [[0 for _ in range(m)]]

wonpan.extend([insp() for _ in range(n)] + [[0 for _ in range(m)]])

near = lambda x : x % m if x >= 0 else m - 1

for x,d,k in [insp() for _ in range(t)]:
    for i in range(n + 1):
        if not i % x:
            spl = m-(k % m) if not d else k % m
            wonpan[i] = wonpan[i][spl:] + wonpan[i][:spl]
    
    changed = set()
    for i in range(1, n+1):
        for j in range(m):
            if wonpan[i][j] != 0 and wonpan[i][j] in [wonpan[i-1][j], wonpan[i+1][j], wonpan[i][near(j+1)], wonpan[i][near(j-1)]]:
                qu = deque([(i,j,wonpan[i][j])])
                wonpan[i][j] = 0
                changed.add(i)
                while qu:
                    row, col, num = qu.popleft()
                    for drow, dcol in [[-1,0], [1,0], [0,-1], [0,1]]:
                        nrow,ncol = row+drow, near(col+dcol)
                        if wonpan[nrow][ncol] == num:
                            qu.append((nrow,ncol,wonpan[nrow][ncol]))
                            wonpan[nrow][ncol] = 0
                            changed.add(nrow)
    
    if not changed:
        cnt = 0
        tsum = 0
        for i in range(1, n+1):
            for j in range(m):
                if wonpan[i][j] != 0:
                    tsum += wonpan[i][j]
                    cnt += 1
        if cnt != 0:
            avg = tsum / cnt
            for i in range(1, n+1):
                for j in range(m):
                    if wonpan[i][j] != 0:
                        if wonpan[i][j] > avg:
                            wonpan[i][j] -= 1
                        elif wonpan[i][j] < avg:
                            wonpan[i][j] += 1

print(sum([sum(i) for i in wonpan]))