# [BOJ] 1874. 스택 수열
# 소요 시간 : 00분

num_list = []
n = int(input())
stack = [0]
last = 1
result = []
for _ in range(n):
    num_list.append(int(input()))

for i in num_list:
    if i == stack[-1]:
        stack.pop()
        result.append("-")
    elif i < stack[-1]:
        print("NO")
        break
    else:
        while last <= i:
            stack.append(last)
            result.append("+")
            last += 1
        stack.pop()
        result.append("-")
else:
    for i in result:
        print(i)
