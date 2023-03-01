# [BOJ] 10870. 피보나치 수 5
# 소요 시간 : 10분


def fib(n):
    if n < 2:
        return n
    
    memo = [0, 1]
    
    while len(memo) <= n:
        memo.append(memo[-2] + memo[-1])
    
    return memo[-1]

print(fib(int(input())))