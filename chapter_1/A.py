# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\Chapter-1\A_input.txt', 'r', encoding="utf-8")
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
num_list = [int(item) for item in input().split()]

def insertionSort(A, N):
    print(*A)
    for i in range(1, N):
        v = A[i]
        j = i -1

        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        
        A[j+1] = v

        print(*A)

insertionSort(num_list, N)