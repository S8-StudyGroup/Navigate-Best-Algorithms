# [BOJ] 1963. 소수 경로
# 소요 시간 : 00분

from collections import deque

# Input
case_cnt = int(input())
cases = [tuple(input().split()) for _ in range(case_cnt)]


# find prime_number
is_prime = [True] * 10000

for era_num in range(2, 100):
    if is_prime[era_num]:
        for n in range(2*era_num, 10000, era_num):
            is_prime[n] = False

# bfs
def bfs(start, end):
    que = deque([(start, 0)])
    visited = [False] * 10000
    visited[int(start)] = True

    while que:
        num, cnt = que.popleft()

        if num == end:
            return cnt
        
        for idx in range(4):
            for i in range(10):
                next_num = int(num[:idx] + str(i) + num[idx+1:])
                if not visited[next_num] and is_prime[next_num] and next_num >= 1000:
                    visited[next_num] = True
                    que.append((str(next_num), cnt+1))
    
    return 'Impossible'


# OutPut
for start, end in cases:
    print(bfs(start, end))
