# [BOJ] 15661. 링크와 스타트
# 소요 시간 : 60분

from itertools import combinations

N = int(input())
points = []

for p in range(N):
    temp = list(map(int, input().split()))
    points.append(temp)

people = [i for i in range(N)]

sub_min = 100 * N

for k in range(1, N // 2 + 1):
    for case in combinations(people, k):
        team1 = list(case)
        team2 = list(set(people) - set(case))
        sub1 = 0
        sub2 = 0
        for i in team1:
            for j in team1:
                sub1 += points[i][j]
        for i in team2:
            for j in team2:
                sub2 += points[i][j]
        result = sub1 - sub2
        if result < 0:
            result = result * -1
        if result < sub_min:
            sub_min = result

print(sub_min)