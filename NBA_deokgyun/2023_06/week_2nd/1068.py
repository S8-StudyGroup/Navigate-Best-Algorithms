# [BOJ] 1068. 트리
# 소요 시간 : 00분

def order(v):
    global cnt
    
    if tree[v]:
        for i in tree[v]:
            order(i)
 
    else:
        cnt += 1
 
 
n = int(input())
li = list(map(int, input().split()))
tree = [[] for i in range(n)]
d = int(input())
 
 
a = []
for i in range(n):
    if li[i] == -1:
        a.append(i)
    if li[i] != -1 and i != d:
        tree[li[i]].append(i)
 
cnt = 0
for i in a:
    if i != d:
        order(i)
print(cnt)