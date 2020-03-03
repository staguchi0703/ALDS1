

# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\chapter_4\D_input.txt', 'r', encoding="utf-8")
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
N, k = [int(item) for item in input().split()]
w_list = [int(input()) for _ in range(N)]

w_min = max(w_list)
w_max = sum(w_list)

is_not_just = True


left = w_min
right = w_max

while is_not_just:
    mid = (left + right) // 2

    temp_sum = 0
    temp_res = 0
    cnt = 0
    for item in w_list:
        temp_sum += item
        if temp_sum > mid:
            temp_res = max(temp_sum, temp_res)
            temp_sum = 0
            cnt += 1
            print('temp_res', temp_res)
            print('cnt', cnt)
    cnt += 1
    if cnt > k:
        left = mid
    elif cnt < k:
        right = mid
    else:
        print(temp_res)
        is_not_just = False


