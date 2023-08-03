# [BOJ] 25601. 자바의 형변환
# 소요 시간 : 00분
import sys
input = sys.stdin.readline

n = int(input())

graph = {}
for _ in range(n-1):
    child, parent = input().split()
    graph[child] = parent

a, b = input().split()
answer = 0


def check_casting(child, parent):
    while child != parent:
        if graph.get(child) is None:
            return False
        child = graph[child]

    return True


if check_casting(a, b) or check_casting(b, a):
    answer = 1

print(answer)
