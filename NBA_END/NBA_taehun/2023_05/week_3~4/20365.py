# [BOJ] 20365. 블로그2
# 소요 시간 : 00분

import sys
input = sys.stdin.readline

n = int(input().strip())
# string = list(map(str, input().strip()))
string = input().strip()

dict_color = {'B':0, 'R':0}

state = None
for i in range(n):
    if string[i] == 'B' and state != 'B':
        dict_color['B'] += 1
        state = 'B'
    elif string[i] == 'R' and state != 'R':
        dict_color['R'] += 1
        state = 'R'
print(min(dict_color['B'], dict_color['R']) + 1)