# [BOJ] 15656. N과 M (7)
# 소요 시간 : 00분

def dfs(node, seq=()):
    seq = (*seq, node)

    if len(seq) == M:
        print(*seq)
        return
    
    for next_num in nums:
        dfs(next_num, seq)


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

for num in nums:
    dfs(num)