# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\chapter_3\A_input.txt', 'r', encoding="utf-8")
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

letter = input().split(' ')
stack = collections.deque()

cnt = 0
eq = ''

while stack:

    temp = letter.pop()
    stack.append(temp)
        
    if temp in ['+', '-', '*']:
        pass
    else:
        cnt += 1

        if cnt == 2:
            for i in range(3):
                eq += stack.pop)

            cnt = 0

