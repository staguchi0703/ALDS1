# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\chapter_6\D_input.txt', 'r', encoding="utf-8")
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

def main():
    import collections

    N = int(input())
    w_list = [int(item) for item in input().split()]

    # 方針
    # 最も重いものの動かす回数を最小にする
    # 最も重いものを選んでstackへ詰める
    # 入れ替えたモノの位置更新と最重をのぞいたリストにする
    # リストが空になるまでやる

    stack = collections.deque()
    temp_list = w_list
    cost = 0
    while len(temp_list)>1:
        temp_max = max(temp_list)
        max_index = temp_list.index(temp_max)
        stack.appendleft(temp_max)

        if max_index != len(temp_list) - 1:
            last_num = temp_list[-1]
            temp_list[max_index] = last_num
            cost += temp_max + last_num
            
        temp_list.pop()
    stack.appendleft(temp_list[0])

    print(cost)

    return cost

if __name__ == "__main__":
    main()