# [BOJ] 15656. N과 M (7)
# 소요 시간 : 60+분

def pick(depth):
    global N, M
    if depth == M:
        print(*result)
        return

    for n in numbers:
        result.append(n)
        pick(depth + 1)
        result.pop()


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
result = []
pick(0)