# [BOJ] 16722. 결! 합!
# 소요 시간 : 00분
import sys
from itertools import combinations
input = sys.stdin.readline


def check_hap(a, b, c):
    """_summary_
    '합'을 만족하는지 확인하는 함수
    """
    for i in range(3):
        if paint[a][i] == paint[b][i] == paint[c][i] or paint[a][i] != paint[b][i] != paint[c][i] != paint[a][i]:
            continue
        else:
            return False

    return True


def check_gyeol():
    """_summary_
    '결'을 만족하는지 확인하는 함수
    """
    if sorted(hap_visited) == hap_list:
        return True
    else:
        return False


paint = [list(input().split(' ')) for _ in range(9)]
hap_list = []

for i in combinations(range(9), 3):
    if check_hap(*i):
        hap_list.append(list(i))

n = int(input())
score = 0
hap_visited = []
is_gyeol = False

for _ in range(n):
    temp = input().split()

    if temp[0] == 'H':
        a, b, c = map(int, temp[1:])
        cur_hap = sorted([a - 1, b - 1, c - 1])
        if cur_hap in hap_list and cur_hap not in hap_visited:
            hap_visited.append(cur_hap)
            score += 1
        else:
            score -= 1

    elif temp[0] == 'G':
        if check_gyeol() and not is_gyeol:
            is_gyeol = True
            score += 3
        else:
            score -= 1

print(score)
