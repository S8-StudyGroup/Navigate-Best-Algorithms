# [BOJ] 15661. 링크와 스타트
# 소요 시간 : 00분

import sys
from itertools import combinations

def chk(team):
    count = 0
    for case in combinations(team, 2):
        if case not in visited:
            count += arr[case[0]][case[1]]
            visited.add(case)
    return count

input = sys.stdin.readline

N = int(input().strip())

arr = [list(map(int, input().strip().split())) for _ in range(N)]

for r in range(N):
    for c in range(r):
        arr[c][r] += arr[r][c]

result = 9999999999
checked = set()
for i in range(N//2, 1, -1):
    if result == 0:
            break
    for case in combinations(range(N), i):
        if result == 0:
            break
        if case not in checked:
            visited = set()
            team1 = set(case)
            team2 = set(range(N)) - team1
            diff = abs(chk(team1) - chk(team2))
            result = min(result, diff)
            checked.add(case)
            checked.add(tuple(team2))

print(result)
