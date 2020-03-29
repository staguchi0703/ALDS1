def resolve():
    '''
    code here
    '''
    import sys
    import heapq
    queries = sys.stdin.readlines()
    
    heap = []

    for line in queries:
        query, *val = line.split()
        
        if query == 'insert':
            value = -1 * int(val[0])
            heapq.heappush(heap, value)
        if query == 'extract':
            print(-1 * heapq.heappop(heap))

    # print(heap)

if __name__ == "__main__":
    resolve()
