# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\chapter_5\C_input.txt', 'r', encoding="utf-8")
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
import numpy as np
N = int(input())
X = np.array([0., 0.])
Y = np.array([100., 0.])

rad = np.pi / 2 * 2 /3

rot = np.array([
    [np.cos(rad), np.sin(rad)],
    [-1 * np.sin(rad), np.cos(rad)]
    ])

def coh(left, right, cnt):
    if cnt == N:
        return

    cnt += 1

    s = (left + right) / 3
    t = (left + right) /3 * 2
    u = (t - s) @ rot + s

    print(*left)
    print(*s)
    print(*u)
    print(*t)
    print(*right)

    coh(s, u, cnt)
    coh(u, t, cnt) 

coh(X, Y, 0)

