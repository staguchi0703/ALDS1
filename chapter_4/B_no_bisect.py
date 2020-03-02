# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\chapter_4\B_input.txt', 'r', encoding="utf-8")
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
S = [int(item) for item in input().split()]
q = int(input())
T = [int(item) for item in input().split()]

def bisect(S, x):
    search_list = S[:]

    while len(search_list) > 1:
        mid = len(search_list)//2
        # print(mid, search_list[mid])
        if x < search_list[mid]:
            search_list = search_list[:mid]
        elif x > search_list[mid]:
            search_list = search_list[mid:]
        else:
            return 1
    return 0
    

cnt = 0
for i in range(q):
    temp_num = T[i]
    cnt += bisect(S, temp_num)
print(cnt)
