# [BOJ] 2661. ⚾
# 소요 시간 : 00분
import sys
from itertools import permutations
input = sys.stdin.readline

inning_cnt = int(input())
innings = [list(map(int, input().split())) for _ in range(inning_cnt)]

max_score = 0

def get(hitter_stats):
    hitter_idx = 0
    score = 0
    for inning in innings:
        outcount = 0
        base1, base2, base3 = 0, 0, 0
        while outcount < 3:
            if inning[hitter_stats[hitter_idx]] == 0:
                outcount += 1
            elif inning[hitter_stats[hitter_idx]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif inning[hitter_stats[hitter_idx]] == 2:
                score += (base2 + base3)
                base1, base2, base3 = 0, 1, base1
            elif inning[hitter_stats[hitter_idx]] == 3:
                score += (base2 + base3 + base1)
                base1, base2, base3 = 0, 0, 1
            elif inning[hitter_stats[hitter_idx]] == 4:
                score += (1 + base1 + base2 + base3)
                base1, base2, base3 = 0, 0, 0
            
            hitter_idx = (hitter_idx + 1) % 9
    return score
        
for hitter_stats in permutations(range(1,9), 8):
    hitter_stats = list(hitter_stats[:3]) + [0] + list(hitter_stats[3:])
    max_score = max(max_score, get(hitter_stats))

print(max_score)
