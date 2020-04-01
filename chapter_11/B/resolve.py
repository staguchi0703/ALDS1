def resolve():
    '''
    code here
    '''
    import collections

    N = int(input())
    adjacency_list = [[int(item) for item in input().split()] for _ in range(N)]

    fp_d = [0 for _ in range(N)]
    fp_f = [0 for _ in range(N)]
    
    stack = collections.deque([1])
    cnt = 1
    while stack:
        temp_node = stack.pop()
        temp_adjacency = adjacency_list[temp_node-1]
        cnt += 1

        if temp_adjacency[1] == 0:
            fp_f[temp_node-1] = cnt 
        else:
            to_nodes = temp_adjacency[2:]
            to_node = to_nodes.pop()
            stack.append(to_node)
            temp_adjacency[1] -= 1

            fp_d[temp_node-1] = cnt 
            adjacency_list[temp_node-1] = temp_adjacency[:2] + to_nodes

    print(fp_d)
    print(fp_f)

if __name__ == "__main__":
    resolve()
