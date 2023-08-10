# [BOJ] 14620. 꽃길
# 소요 시간 : 00분
# 4:00

# import sys

# input = sys.stdin.readline

# def count_price(r, c):
#     result = arr[r][c]
#     for dr, dc in d:
#         nr, nc = r + dr, c + dc
#         result += arr[nr][nc]
#     return result

# def find_best(i, j, count, sum_price, visited):
#     if count == 3:
#         result[-1] = min(result[-1], sum_price)
#         print(t, result[-1])
#         return
#     if sum_price >= result[-1]:
#         return
#     for r in range(i, N-2):
#         for c in range(N-2):
#             if (r, c) not in visited:
#                 check(r, c, visited)
#                 t.add((r,c))
#                 print(count)
#                 print("-----------")
#                 find_best(r, c, count + 1, sum_price+price_map[r][c], visited)
#                 print("============")
#                 print(count)
#                 uncheck(r, c, visited)
#                 if (r, c) in t:
#                     t.remove((r, c))
                
                
# def check(r, c, visited):
#     print(visited)
#     visited.add((r,c))
#     for dr, dc in d:
#         nr, nc = r + dr, c + dc
#         if 0 <= nr < N-2 and 0 <= nc < N-2:
#             visited.add((nr, nc))
#         for ddr, ddc in d:
#             nnr, nnc = nr + ddr, nc + ddc
#             if 0 <= nnr < N-2 and 0 <= nnc < N-2:
#                 visited.add((nnr, nnc))
#     return visited

# def uncheck(r, c, visited):
#     if (r, c) in visited:
#         visited.remove((r, c))
#     for dr, dc in d:
#         nr, nc = r + dr, c + dc
#         if (nr, nc) in visited:
#             visited.remove((nr, nc))
#         for ddr, ddc in d:
#             nnr, nnc = nr + ddr, nc + ddc
#             if 0 <= nnr < N-2 and 0 <= nnc < N-2:
#                 if (nnr, nnc) in visited:
#                     visited.remove((nnr, nnc))
#     return visited
            
    



# N = int(input().strip())
# arr = [list(map(int, input().strip().split())) for _ in range(N)]

# d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# price_map = [[0] * (N-2) for _ in range(N-2)]

# for r in range(1, N-1):
#     for c in range(1, N-1):
#         price_map[r-1][c-1] = count_price(r, c)


# result = [200*5*3]

# t = set()
# find_best(0, 0, 0, 0, set())

# print(result)



import sys

input = sys.stdin.readline

N = int(input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
