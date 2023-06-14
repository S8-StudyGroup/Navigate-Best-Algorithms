# [BOJ] 1068. 트리
# 소요 시간 : 00분

def dfs(num, arr):
    arr[num] = -2
    
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)


n = int(input())
arr = list(map(int, input().split()))
k = int(input())
count = 0

dfs(k, arr)
answer = 0

for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        answer += 1

print(answer)