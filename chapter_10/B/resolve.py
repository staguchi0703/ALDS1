def resolve():
    '''
    code here
    '''
    N = int(input())
    mat = [[int(item) for item in input().split()] for _ in range(N)]

    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in reversed(range(N-2)):
        for j in range(i+2, N):
            dp[i][j] = min(dp[i][j-1] * mat[i][0]*mat[j][0]*mat[j][1],
                            dp[i][j])

        print(dp)
        

if __name__ == "__main__":
    resolve()
