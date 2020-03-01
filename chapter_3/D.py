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

landscape = input()

grid = collections.deque([[0,0]])
temp_max = 0
temp_min = 0

water_area = 0


for i, delta in enumerate(landscape):
    preb = grid[-1][1]
    if delta == '\\':
        grid.append([i+1, preb - 1])
    elif delta == '_':
        grid.append([i+1, preb])
    else:
        grid.append([i+1, preb + 1])

    temp_height = grid[-1][1]

    temp_max = max(temp_max, temp_height)
    temp_min = min(temp_min, temp_height)

    if temp_max >= temp_height:
        if delta == '_':
            water_area += temp_max -temp_height
        elif delta == '\\':
            water_area += (temp_max - temp_height - 1) + 0.5
        elif delta == '/':
            water_area += (temp_max - temp_height) + 0.5

# 左端は水位0以上にはならない
# 右端は最右端の凸ピーク以上にならない
# 　→　水位は右から順に高くなる
#  →　再左端上凸ピークより水位は高くならない
# 　 →　ここと同じ高さを探す
# 　 →　池が完成したら池の幅を探索範囲から消す
#  →　なければ右端上凸ピークとなす水位

print(grid)
