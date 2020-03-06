# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\chapter_6\A_input.txt', 'r', encoding="utf-8")
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

def countingSort(A, k):
    B = [0 for _ in range(N+1)]
    C = [0 for _ in range(k+1)]

    for j in range(N):
        C[A[j]] += 1
    
    for i in range(1, k+1):
        C[i] = C[i] + C[i - 1]

    for j in reversed(range(N)):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1
    return B[1:]


print(*countingSort(num_list, max(num_list)))