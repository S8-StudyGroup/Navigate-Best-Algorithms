# [BOJ] 20365. 블로그2
# 소요 시간 : 00분

color_cnt = input()
colors = input()
red = blue = 0
last = 'Firstcolor'

for color in colors:
    if color == 'B':
        if last != color:
            blue += 1
    else:
        if last != color:
            red += 1
    last = color

print(min(red, blue) + 1)