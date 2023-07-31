# [BOJ] 1074. Z
# 소요 시간 : 00분
import sys
input = sys.stdin.readline


def Z(n: int, r: int, c: int):
    """_summary_

    Args:
        n (int): 2^n
        r (int): row
        c (int): col

    Returns:
        _type_: r행 c열을 몇 번째로 방문
    """
    
    # 종료 조건
    if n == 0:
        return 0
    
    half = 2 ** (n-1)
    subarray = (r >= half) * 2 + (c >= half)
    """_summary_
    subarray가 0일 경우: 현재 위치 (r, c)가 크기 2^n인 격자의 좌상단 구역에 속함
    subarray가 1일 경우: 현재 위치 (r, c)가 크기 2^n인 격자의 우상단 구역에 속함
    subarray가 2일 경우: 현재 위치 (r, c)가 크기 2^n인 격자의 좌하단 구역에 속함
    subarray가 3일 경우: 현재 위치 (r, c)가 크기 2^n인 격자의 우하단 구역에 속함
    """
    subarray_r = r % half
    subarray_c = c % half
    return ((subarray * half * half)
            + Z(n-1, subarray_r, subarray_c))


n, r, c = map(int, input().split())
print(Z(n, r, c))
