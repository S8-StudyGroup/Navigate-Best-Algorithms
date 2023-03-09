# [BOJ] 10870. 피보나치 수 5
# 소요 시간 : 00분

def fibonacci(n):
   if n == 0:
       return 0
   if n == 1:
       return 1
   else:
       return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(int(input())))