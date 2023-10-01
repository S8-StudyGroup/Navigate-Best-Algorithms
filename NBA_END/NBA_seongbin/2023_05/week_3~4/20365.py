# [BOJ] 20365. 블로그2
# 소요 시간 : 20분
# 아이디어 1. 연속된 색은 하나로 생각하기.
# 아이디어 2. 가장 빠른 방법은 시작 색을 다 칠하고 나머지 색을 칠하는 것.

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
problems = list(input().strip())

problems = [problems[0]] + [problems[i]
                            for i in range(1, N) if problems[i] != problems[i-1]]

if len(problems) == 1:
    print(1)
else:
    second_color_cnt = problems.count(problems[1])

    print(1 + second_color_cnt)
