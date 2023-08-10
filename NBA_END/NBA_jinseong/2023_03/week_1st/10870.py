# [BOJ] 10870. 피보나치 수 5
# 소요 시간 : 10분

def fibonacci(n):
    if n in store.keys():
        return store[n]
    if n < 2:
        return n
    store[n] = fibonacci(n-2) + fibonacci(n-1)
    return store[n]


N = int(input())
store = {}
ans = fibonacci(N)

print(ans)
