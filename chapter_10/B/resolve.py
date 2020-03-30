def resolve():
    '''
    code here
    '''
    N = int(input())
    input_matrix = [[int(item) for item in input().split()] for _ in range(N)]

    memo = [[0,0] for _ in range(N)]

    for i, matrix in enumerate(input_matrix):

        memo[i][0] = [int(item) for item in matrix.split()]
        if i == 0:
            memo[i][1] = 1
        else:
            first_num = memo[i-1][0][0]
            second_num = memo[i][0][0]
            memo[i][1] = memo[i-1][1]*first_num*second_num
    print(memo)

if __name__ == "__main__":
    resolve()
