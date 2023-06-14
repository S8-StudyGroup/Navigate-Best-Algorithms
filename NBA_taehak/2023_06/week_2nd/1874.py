# [BOJ] 1874. 스택 수열
# 소요 시간 : 00분

n = int(input())
stack = []
answer = []
memo = 0
now = 1

for i in range(n):
    num = int(input())

    while now <= num:
        stack.append(now)
        answer.append("+")
        now += 1

    if stack[-1] == num:
        stack.pop() 
        answer.append("-")
    else:   
        print("NO")
        memo = 1
        break

if memo == 0:
    for i in answer:
        print(i)