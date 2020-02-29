# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\chapter_3\B_input.txt', 'r', encoding="utf-8")
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
import collections

N, q = [int(item) for item in input().split()]
input_list = [[item for item in input().split()] for _ in range(N)]

que = collections.deque()
for p, time in input_list:
    que.append([p, int(time)])

finish_time = 0
while que:
    temp = que.popleft()

    if temp[1] - q <= 0:
        finish_time += temp[1]
        print(temp[0], finish_time)

    else:
        finish_time += q
        temp[1] -= q
        que.append(temp)




