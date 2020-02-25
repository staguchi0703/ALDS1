# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\chapter_2\D_input.txt', 'r', encoding="utf-8")
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
N = int(input())
num_list = [int(input()) for _ in range(N)]

def insertionSort(A, N, g):
    cnt = 0
    for i in range(g, N):
        v = A[i]
        j = i -g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j -g
            cnt += 1
        A[j+g] = v
    return A, cnt


def shellSort(A, N):
    cnt = 0
    m = N//2
    G = A[0:m]
    for i in range(m):
        A, temp_cnt = insertionSort(A, N, G[i])
        cnt = temp_cnt
    return  m, G, cnt, A,

print(shellSort(num_list, N))
