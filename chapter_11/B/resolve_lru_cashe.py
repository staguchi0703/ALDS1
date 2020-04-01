def resolve():
    '''
    code here
    '''
    from functools import lru_cache
    N = int(input())

    @lru_cache(maxsize=10000000)
    def fina(n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        
        return fina(n-1) + fina(n-2)
    
    print(fina(N))



if __name__ == "__main__":
    resolve()
