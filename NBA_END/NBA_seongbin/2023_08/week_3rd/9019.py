# [BOJ] 9019. DSLR
# 소요 시간 : 30분
import sys
from collections import deque
input = sys.stdin.readline

CMD_LIST = ['D', 'S', 'L', 'R']
CMD_DEF = {
    'D': lambda x: (x * 2) % 10000,
    'S': lambda x: 9999 if x == 0 else x - 1,
    'L': lambda x: (x % 1000) * 10 + x // 1000,
    'R': lambda x: (x % 10) * 1000 + x // 10
}


def bfs(A, cmd):
    queue = deque([(A, '')])
    visited = [False] * 10000
    visited[A] = True

    while queue:
        cur, cmd = queue.popleft()
        if cur == B:
            return cmd

        for CMD in CMD_LIST:
            next = CMD_DEF[CMD](cur)
            if not visited[next]:
                visited[next] = True
                next_cmd = cmd + CMD
                queue.append((next, next_cmd))


T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    answer = bfs(A, '')

    print(answer)
