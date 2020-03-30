def resolve():
    '''
    code here
    '''
    import collections
    N = int(input())
    A_list = [input() for _ in range(N)]

    def lcs(a, b):
        num_a = len(a)
        num_b = len(b)
        dp = [[0 for _ in range(num_b+1)] for _ in range(num_a+1)]
        
        for i in range(num_a):
            for j in range(num_b):
                if a[i+1] == b[j+1]:
                    dp[i+1][j+1] = 1
                
                for k in range(num_b):
                    dp[i+1][k] = dp[i][k] + dp[i+1][k]
                
                dp[i+1][j+1] = max(dp[i+1][j], dp[i+1][j+1])
                    
    for i in range(N):
        print(lcs(A_list[2*i], A_list[2*i+1]))

if __name__ == "__main__":
    resolve()
