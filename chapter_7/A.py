# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\chapter_7\A_input.txt', 'r', encoding="utf-8")
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
    N = int(input())
    node_attr_list = [[int(item) for item in input().split()] for _ in range(N)]

    tree = [[0, -1, 0, [], False] for _ in range(N)] # [node, parent, depth, [*child_node], foot print]

    for i, node_attr in enumerate(node_attr_list):
        tree[i][0] = node_attr[0]

        if tree[i][1] != 0:
            tree[i][3] = node_attr[2:]

    
    def dfs(node, depth, parent, child):
        # print(node, depth, parent, child)
        tree[node][4] = True
        if child == []:
            tree[node][1] = parent
            tree[node][2] = depth
            return


        tree[node][1] = parent
        tree[node][2] = depth
        for item in child:
            dfs(item, depth+1, node, tree[item][3])

    def all(iterable):
        for element in iterable:
            if not element[4]:
                return False
        return True

    for i in range(N):
        for j in range(N):
            tree[j][4] = False

        dfs(i, 0, -1, tree[i][3])

        if all(tree):
            break

    for node in tree:
        print('node {}:'.format(node[0]), end=' ')
        print('parent =', node[1], end=', ')
        print('depth =', node[2], end=', ')
        if node[3] == [] and node[1] != -1:
            print('leaf', end=', ')
        elif node[3] and node[1] != -1:
            print('internal node', end=', ')
        else:
            print('root', end=', ')
        print(node[3])

if __name__ == "__main__":
    main()


