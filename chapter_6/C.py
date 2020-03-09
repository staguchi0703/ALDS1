# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\chapter_6\C_input.txt', 'r', encoding="utf-8")
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
import sys
sys.setrecursionlimit(2000)

N = int(input())
origin_list = [input().split() for _ in range(N)]
card_list = origin_list[:]

def partition(A, p, r):
    x = int(A[r][1])
    i = p - 1

    for j in range(p, r):
        if int(A[j][1]) <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

quickSort(card_list, 0, len(card_list)-1)

sorce_list = ['' for _ in range(N)]
test_list = ['' for _ in range(N)]

temp_num = 0
cnt = 0
for i in range(N):
    if test_list[i][1] > temp_num:
        temp_num = test_list[i][1]
        cnt += 1
    else:
        sorce_list[cnt] += 



    index = int(origin_list[i][1])
    sorce_list[index] += origin_list[i][0]+origin_list[i][1]

    index2 = int(card_list[i][1])
    test_list[index2] += card_list[i][0]+card_list[i][1] 


if sorce_list == test_list:
    print('Stable')
else:
    print('Not stable')

for item in card_list:
    print(*item)
