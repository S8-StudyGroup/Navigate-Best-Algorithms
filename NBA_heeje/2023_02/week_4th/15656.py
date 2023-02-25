# [BOJ] 15656. N과 M (7)
# 소요 시간 : 20분



def dfs(ans_list):
    if len(ans_list) == M:
        print(*ans_list)
        return
    
    for number in numbers:
        dfs(ans_list + [number])

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))

dfs([])