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
q = int(input())
q_list = [int(item) for item in input().split()]


deque = []
for i in range(1,2**N):
    temp_num = 0
    for j in range(N):
        if (i >> j) & 1 == 1:
            temp_num += num_list[j]
    deque.append(temp_num)

# res_list = list(deque)
for k in q_list:
    if k in deque:
        print('yes')
    else:
        print('no')

