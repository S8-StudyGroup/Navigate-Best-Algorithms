# [Programmers] 1843. 사칙연산
# 소요 시간 : 00분

from collections import deque

def solution(arr):
    table = {"+": (lambda x, y: x + y), "-": (lambda x, y: x - y)}
    dq = deque(arr)
    result = 0
    while dq:
        number = dq.popleft()
        operator = dq.popleft()
        


    
    return

def find_minus(idx, arr):
    for i in range(idx+1:)


print(solution(["1", "-", "3", "+", "5", "-", "8"]))
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))