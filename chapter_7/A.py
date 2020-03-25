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

    print(tree)
if __name__ == "__main__":
    main()


# node 0: parent = -1, depth = 0, root, [1, 4, 10]
# node 1: parent = 0, depth = 1, internal node, [2, 3]
# node 2: parent = 1, depth = 2, leaf, []
# node 3: parent = 1, depth = 2, leaf, []
# node 4: parent = 0, depth = 1, internal node, [5, 6, 7]
# node 5: parent = 4, depth = 2, leaf, []
# node 6: parent = 4, depth = 2, leaf, []
# node 7: parent = 4, depth = 2, internal node, [8, 9]
# node 8: parent = 7, depth = 3, leaf, []
# node 9: parent = 7, depth = 3, leaf, []
# node 10: parent = 0, depth = 1, internal node, [11, 12]
# node 11: parent = 10, depth = 2, leaf, []
# node 12: parent = 10, depth = 2, leaf, []