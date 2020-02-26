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
stack = collections.deque(letter.pop())


def calc_chk(num1, num2, op):
    if op in ['+', '-', '*'] and num1 not in ['+', '-', '*'] and num2 not in ['+', '-', '*']:
        return True
    else:
        return False

while letter:
    temp = letter.pop()
    stack.append(temp)

    is_calc = True
    while is_calc:
        # print(stack)
        if len(stack) >=3:
            if calc_chk(stack[-1], stack[-2], stack[-3]):
                num1 = stack.pop()
                num2 = stack.pop()
                op = stack.pop()
                val = str(eval(num1 + op + num2))
                stack.append(val)
    
            else:
                is_calc = False
        else:
            is_calc = False
print(*stack)