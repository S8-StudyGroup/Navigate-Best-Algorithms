# [BOJ] 1963. 소수 경로
# 소요 시간 : 30분

from collections import deque

def is_prime(n:int) -> bool:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False    
    return True


def dfs(start):
    queue = deque()
    queue.append((start, 0))
    visited = set()
    visited.add(int(start))

    while queue:
        num, time = queue.popleft()

        if num == end:
            return time

        for i in range(0, 10):
            for j in range(4):
                n_num = int(num[:j] + str(i) + num[j + 1:])
                
                if n_num < 1000: continue
                if n_num in visited: continue
                visited.add(n_num)

                if is_prime(n_num):
                    queue.append((str(n_num), time + 1))
    
    return -1



T = int(input())
for _ in range(T):
    start, end = input().split()
    answer = dfs(start)
    print(answer if answer != -1 else "Impossible")
