def resolve():
    '''
    code here
    '''
    import collections
    N = int(input())
    A_list = [[int(item) for item in input().split()] for _ in range(N)]
    A_list.sort(key=lambda x:x[0])


if __name__ == "__main__":
    resolve()
