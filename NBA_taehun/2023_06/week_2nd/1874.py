# [BOJ] 1874. 스택 수열
# 소요 시간 : 00분

import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
cnt = 1
result = []
breaker = False
for i in arr:
    if breaker:
        break
    while True:
        # stack의 마지막 숫자가 현재 숫자보다 작아질 때 까지 push
        if not stack or stack[-1] < i:
            stack.append(cnt)
            result.append('+')
            cnt += 1
        else:
            # 현재 수열과 같은 숫자가 있으면 pop
            if stack[-1] == i:
                stack.pop()
                result.append('-')
                break
            # 못찾으면 불가능
            else:
                print('NO')
                breaker = True
                break
else:
    print(*result, sep='\n')
