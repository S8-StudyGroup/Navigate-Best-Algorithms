# [BOJ] 20365. 블로그2
# 소요 시간 : 10분

# 색깔이 변할 때마다 카운트
# 두 색깔 중 적게 나온것 + 1

import sys
input = sys.stdin.readline

N = int(input().strip())
problems = input().strip()
blue_cnt = red_cnt = 0
last = ""

for problem in problems:
    if problem == "B" and last != "B":
        blue_cnt += 1
        last = "B"
    elif problem == "R" and last != "R":
        red_cnt += 1
        last = "R"

print(min(blue_cnt, red_cnt) + 1)