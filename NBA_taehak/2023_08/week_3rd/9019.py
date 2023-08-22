# [BOJ] 9019. DSLR
# 소요 시간 : 00분
from collections import deque

# Input
case_cnt = int(input())
cases = [tuple(map(int, input().split())) for _ in range(case_cnt)]


# DSLR
def DDD(n):
    return (n * 2) % 10000


def SSS(n):
    answer = n - 1
    if n == 0:
        answer = 9999
    return answer


def LLL(n):
    return (n % 1000) * 10 + n // 1000


def RRR(n):
    return (n % 10) * 1000 + n // 10


# bfs
def bfs(a, b):
    que = deque([(a, '')])
    visited = set()

    while True:
        num, command = que.popleft()

        if num == b:
            return command

        next_num = DDD(num)
        if next_num not in visited:
            visited.add(next_num)
            que.append((next_num, command + 'D'))

        next_num = SSS(num)
        if next_num not in visited:
            visited.add(next_num)
            que.append((next_num, command + 'S'))

        next_num = LLL(num)
        if next_num not in visited:
            visited.add(next_num)
            que.append((next_num, command + 'L'))

        next_num = RRR(num)
        if next_num not in visited:
            visited.add(next_num)
            que.append((next_num, command + 'R'))


# Output
for a, b in cases:
    print(bfs(a, b))