def resolve():
    '''
    code here
    '''
    N = int(input())
    mat = [[int(item) for item in input().split()] for _ in range(N)]

    dp = [[1 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(N-1):
        dp[i][i+1] = mat[i][0] * mat[i+1][0] * mat[i+1][1] 

    print(dp)
    for i in reversed(range(N-2)):
        dp[i] = dp[i+1] 
        print(dp)
        for j in range(i+2, N):
            dp[i][j] = min(dp[i][j-1] * mat[i][0]*mat[j][0]*mat[j][1],
                            dp[i][j])

        print(dp)
        

if __name__ == "__main__":
    resolve()
