def resolve():
    '''
    code here
    '''
    import sys

    N = int(input())
    adjacency_list = [[int(item) for item in input().split()] for _ in range(N)]

    adjacency_mat = [[0 for _ in range(N)] for _ in range(N)]

    for i, adjacency in enumerate(adjacency_list):
        if adjacency[1] != 0:
            for j in adjacency[2:]:
                adjacency_mat[i][j-1] = 1

    for item in adjacency_mat:
        print(*item)

if __name__ == "__main__":
    resolve()
