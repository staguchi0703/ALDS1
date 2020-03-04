# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\chapter_5\B_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
# import collections
from functools import lru_cache
N = int(input())
num_list = [int(item) for item in input().split()]


def merge(A, left, mid, right):

    L = A[left : mid] + [100**5]
    R = A[mid: right] + [100**5]
 
    cnt = 0
    i, j = 0, 0
    for k in range(left, right):
        cnt += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        # print(A, left, mid, right)
    return cnt


def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right)//2
        cnt_L = mergeSort(A, left, mid)
        cnt_R = mergeSort(A, mid, right)
        return merge(A, left, mid, right) + cnt_L + cnt_R
    return 0


res_cnt = mergeSort(num_list, 0, N)
print(*num_list)
print(res_cnt)

