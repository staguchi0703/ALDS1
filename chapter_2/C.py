# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\chapter_2\C_input.txt', 'r', encoding="utf-8")
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
A = [[i for i in item] for item in input().split()]

# print(A)

def bubbleSort(A, N):
    is_flag = 1
    cnt = 0

    while is_flag:
        is_flag = 0
        for i in range(N-1):
            if A[i][1] > A[i+1][1]:
                A[i], A[i+1] = A[i+1], A[i]
                is_flag = 1

    res = []
    for item in A:
        temp_res = ''
        for i in item:
            temp_res += i
        res.append(temp_res)
    print(*res)


def selectionSort(A, N):
    cnt = 0
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j][1] < A[minj][1]:
                minj = j
        if i != minj:
            A[i], A[minj] = A[minj], A[i]
    
    res = []
    for item in A:
        temp_res = ''
        for i in item:
            temp_res += i
        res.append(temp_res)
    print(*res)

bubbleSort(A, N)
selectionSort(A, N)