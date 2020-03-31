def resolve():
    '''
    code here
    '''
    from sys import stdin
    N = int(input())
    def lcs(a, b):
        num_a = len(a)
        num_b = len(b)
        dp2 = [0]*(num_b+1)
        
        for i in range(num_a):
            dp1 = dp2[:]
            for j in range(num_b):
                if dp2[j] >= dp1[j+1]: dp2[j+1] = dp2[j]
                else: dp2[j+1] = dp1[j+1]
                
                if a[i] == b[j]:
                    if dp2[j+1] >= dp1[j]+1: dp2[j+1] = dp2[j+1]
                    else: dp2[j+1] = dp1[j]+1
        return dp2[num_b]

    for _ in range(N):
        print(lcs(stdin.readline().strip(), stdin.readline().strip()))

if __name__ == "__main__":
    resolve()
