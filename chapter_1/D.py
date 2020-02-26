# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\Chapter-1\D_input.txt', 'r', encoding="utf-8")
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

temp_max_val = -1 * 10**9
temp_min = num_list[0]

for i in range(N-1):
    temp_max_val = max(temp_max_val, num_list[i+1] - temp_min)
    temp_min = min(temp_min, num_list[i+1])
    # print(temp_min)
    # print(temp_max_val)

print(temp_max_val)