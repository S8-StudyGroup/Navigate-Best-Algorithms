# [BOJ] 1874. 스택 수열
# 소요 시간 : 00분
import sys
input = sys.stdin.readline

t = int(input())
li = []
cnt = 0
print_li = []
X = True

for _ in range(t):
  n = int(input())

  while cnt < n:
    cnt += 1
    li.append(cnt)
    print_li.append('+')

  if li[-1] == n:
    li.pop()
    print_li.append('-')

  else:
    X = False
    break

if X == False:
  print('NO')

else:
  for i in print_li:
    print(i)
