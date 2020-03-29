def resolve():
    '''
    code here
    '''
    import heapq
    N = int(input())
    input_list = [-1 * int(item) for item in input().split()]

    heapq.heapify(input_list)

    input_list = [-1 * item for item in input_list]
    print('', *input_list)


if __name__ == "__main__":
    resolve()
