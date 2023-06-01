# [BOJ] 15661. 링크와 스타트
# 소요 시간 : 20분

from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
min_difference = 99999999

for cnt_member in range(2, N // 2 + 1):
    for start_team in combinations(range(N), cnt_member):
        link_team = set(range(N)) - set(start_team)
        power_start = 0
        power_link = 0
        
        for y, x in combinations(start_team, 2):
            power_start += matrix[y][x] + matrix[x][y]

        for y, x in combinations(link_team, 2):
            power_link += matrix[y][x] + matrix[x][y]
    
        min_difference = min(min_difference, abs(power_start - power_link))

print(min_difference)