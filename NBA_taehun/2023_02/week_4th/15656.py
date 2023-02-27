# [BOJ] 15656. N과 M (7)
# 소요 시간 : 00분

import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().strip().split())
numbers = list(map(int, input().strip().split()))
result = []

[ for permutations(numbers, M)]
    