def resolve():
    '''
    code here
    '''
    N = int(input())
    heap_list = [int(item) for item in input().split()]

    for i, val in enumerate(heap_list):
        print('node {}: key = {}, '.format(i+1,val), end='')
        if (i - 1) // 2 >= 0:
            print('parent key = {}, '.format(heap_list[(i - 1) // 2]), end='')

        left_index = 2*i + 1
        if left_index < N:
            print('left key = {}, '.format(heap_list[left_index]), end='')

        right_index = 2*i + 2
        if right_index < N:
            print('right key = {}, '.format(heap_list[right_index]), end='')
        print('')


if __name__ == "__main__":
    resolve()
