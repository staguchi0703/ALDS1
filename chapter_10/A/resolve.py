def resolve():
    '''
    code here
    '''
    import sys

    sys.setrecursionlimit(100000000)
    N = int(input())

    memo = [0 for _ in range(N+1)]

    def fina(n):
        if n <= 1:
            memo[n] = 1
            return 1

        if memo[n] != 0:
            return memo[n]

        memo[n-1] = fina(n-1)
        memo[n-2] = fina(n-2)        
        memo[n] = memo[n-1] + memo[n-2]

        return memo[n]
    
    print(fina(N))



if __name__ == "__main__":
    resolve()
