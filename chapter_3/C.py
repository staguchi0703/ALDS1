# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\chapter_3\C_input.txt', 'r', encoding="utf-8")
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
com_list = [input().split() for _ in range(N)]
insert_list = [item for item in com_list if item[0] == 'insert']

for com in [item for item in com_list if item[0] != 'insert']:
    print(com)
    print(insert_list)
    if com[0] == 'delete':
        try:
            insert_list.remove(['insert', com[1]])
        except:
            pass

    elif com[0] == 'deleteFirst':
        insert_list = insert_list[1:]

    elif com[0] == 'deleteLast':
        insert_list = insert_list[:-1]

print(*[item[1] for item in insert_list])
# insert x: 連結リストの先頭にキー x を持つ要素を継ぎ足す。
# delete x: キー x を持つ最初の要素を連結リストから削除する。そのような要素が存在しない場合は何もしない。
# deleteFirst: リストの先頭の要素を削除する。
# deleteLast: リストの末尾の要素を削除する。


