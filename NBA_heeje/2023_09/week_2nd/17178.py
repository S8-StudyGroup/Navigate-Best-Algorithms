# [BOJ] 17178. 줄 서기
# 소요 시간 : 00분

import sys
input = sys.stdin.readline

N = int(input())
lines = []
stack = []
answer = "GOOD"

for _ in range(N):
    line = input().split()
    lines.extend(line)

sorted_lines = sorted(lines, key=lambda x: (x[0], int(x[2:])))
lines = lines[::-1]
for target in sorted_lines:
    while True:
        if target in stack:
            if sorted_lines.index(stack[-1]) > sorted_lines.index(target):
                answer = "BAD"
                break
            else:
                stack.pop()
                break
        else:
            if target == lines[-1]:
                lines.pop()
                break
            else:
                stack.append(lines.pop())
    if answer == "BAD":
        break
print(answer)