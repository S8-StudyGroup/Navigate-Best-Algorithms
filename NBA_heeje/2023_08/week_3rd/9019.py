# [BOJ] 9019. DSLR
# 소요 시간 : 20분

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, end):
    queue = deque()
    queue.append((start, ""))
    visited = set()
    visited.add(start)

    while queue:
        n, command = queue.popleft()

        if n == end:
            return command
        
        D = (2 * n) % 10000
        if D not in visited:
            visited.add(D)
            queue.append((D, command + "D"))
        
        S = n - 1 if n != 0 else 9999
        if S not in visited:
            visited.add(S)
            queue.append((S, command + "S"))
        
        str_n = str(n).zfill(4)
        L = int(str_n[1:] + str_n[0])
        if L not in visited:
            visited.add(L)
            queue.append((L, command + "L"))
        
        R = int(str_n[-1] + str_n[:3])
        if R not in visited:
            visited.add(R)
            queue.append((R, command + "R"))


T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    print(bfs(A, B))