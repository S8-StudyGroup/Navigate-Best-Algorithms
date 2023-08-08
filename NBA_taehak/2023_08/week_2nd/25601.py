# [BOJ] 25601. 자바의 형변환
# 소요 시간 : 00분
import sys
input = sys.stdin.readline

# Input
class_cnt = int(input())
graph = {}
for _ in range(class_cnt-1):
    child, parent = input().split()
    graph[child] = parent
A, B = input().split()

# updown
def updown(child, parent):
    while child != parent:
        if graph.get(child) is None:
            return False
        child = graph[child]
    return True


# Output
answer = 0
if updown(A, B) or updown(B, A):
    answer = 1

print(answer)