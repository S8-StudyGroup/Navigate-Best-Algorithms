# [BOJ] 15656. N과 M (7)
# 소요 시간 : 00분

# import sys
# from itertools import product

# input = sys.stdin.readline

# n, m = map(int, input().split())

# numbers = sorted(list(map(int, input().split())))

# for case in product(numbers, repeat=m):
#     print(*case)


import sys

input = sys.stdin.readline

def dfs(temp, depth):
    if depth >= m:
        result.append(temp)
        return
    for number in numbers:
        temp.append(number)
        dfs(temp[:], depth + 1)
        temp.pop()


n, m = map(int, input().split())

numbers = sorted(map(int, input().split()))
result = []
dfs([], 0)
for r in result:
    print(*r)