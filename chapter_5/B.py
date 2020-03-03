# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\chapter_5\A_input.txt', 'r', encoding="utf-8")
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
N = int(input())
num_list = [int(item) for item in input().split()]


def merge(A, left, mid, right):


    L = A[:mid]
    R = A[mid:]
    L.append(10**10)
    R.append(10**10)

    i, j = 0, 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[j]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right)//2;
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

mergeSort(num_list, 0, N-1)
print(num_list)

