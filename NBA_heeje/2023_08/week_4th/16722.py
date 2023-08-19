# [BOJ] 16722. 결! 합!
# 소요 시간 : 00분

from itertools import combinations
import sys
input = sys.stdin.readline

shape = {"CIRCLE": 1, "TRIANGLE": 2, "SQUARE": 3}
color = {"YELLOW": 1, "RED": 2, "BLUE": 3}
bg_color = {"GRAY": 1, "WHITE": 2, "BLACK": 3}
pictures = []
gyeol = set()

for i in range(1, 10):
    S, C, B = input().split()
    pictures.append((shape[S], color[C], bg_color[B]))

for gyeol_case in combinations(range(9), 3):
    for i in range(3):
        gyeol_sum = 0
        for j in range(3):
            gyeol_sum += pictures[gyeol_case[j]][i]
        
        if gyeol_sum % 3:
            break
    
    else:
        gyeol.add(gyeol_case)

print(gyeol)

n = int(input())
score = 0
is_gyeol = False
for _ in range(n):
    command = input().split()
    if command[0] == "G":
        if len(gyeol) == 0 and not is_gyeol:
            is_gyeol = True
            score += 3
        else:
            score -= 1
    else:
        a, b, c = sorted([int(command[1]) - 1, int(command[2]) - 1, int(command[3]) - 1])
        if (a, b, c) in gyeol:
            score += 1
            gyeol.remove((a, b, c))
        else:
            score -= 1

print(score)
