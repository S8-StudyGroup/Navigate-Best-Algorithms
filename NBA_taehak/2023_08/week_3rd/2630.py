# [BOJ] 2630. 색종이 만들기
# 소요 시간 : 00분

# Input
size_0 = int(input())
paper = [list(map(int, input().split())) for _ in range(size_0)]

# 
white = 0
blue = 0

def check(r, c, size):
  global white, blue

  color = paper[r][c]
  for i in range(r, r+size) :
    for j in range(c, c+size) :
      if color != paper[i][j] :
        check(r, c, size//2)
        check(r, c+size//2, size//2)
        check(r+size//2, c, size//2)
        check(r+size//2, c+size//2, size//2)
        return
  if color == 0 :
    white += 1
  else :
    blue += 1


# Output
check(0, 0, size_0)
print(white)
print(blue)