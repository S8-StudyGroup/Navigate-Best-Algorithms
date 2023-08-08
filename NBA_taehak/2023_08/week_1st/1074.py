# [BOJ] 1074. Z
# 소요 시간 : 00분
N, tr, tc = map(int, input().split())


def search(r=0, c=0, n=N, num=0):
    mid = 2**(n-1)
    plus = (2**(n-1))**2
    # print(r, c, n, num, mid, plus)

    if n == 0:
        print(num)
        return

    # 1사분면
    if tr < r + mid and tc < c + mid:
        search(r, c, n-1, num)
    # 2사분면
    elif tr < r + mid and tc >= c + mid:
        search(r, c+mid, n-1, num + plus)
    # 3사분면
    elif tr >= r + mid  and tc < c + mid:
        search(r+mid, c, n-1, num + 2*plus)
    # 4사분면
    else:
        search(r+mid, c+mid, n-1, num + 3*plus)


search()


























# N, tr, tc = map(int, input().split())

# delta = [(0, 1), (1, 0), (1, 1)]


# def z_square(r, c, square):
#     rcs = [(r, c)]
#     for dr, dc in delta:
#         nr = r + 2**square * dr
#         nc = c + 2**square * dc
#         rcs.append((nr, nc))
#     return rcs


# num = -1


# def go(rr, cc, square):
#     global num
#     if square == 0:
#         for nr, nc in z_square(rr, cc, 0):
#             num += 1
#             if (nr, nc) == (tr, tc):
#                 print(num)
#                 exit()
    
#     else:
#         for nr, nc in z_square(rr, cc, square):
#             go(nr, nc, square-1)


# go(0, 0, N-1)