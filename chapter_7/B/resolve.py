def resolve():
    '''
    code here
    '''
    N = int(input())
    A_list = [[int(item) for item in input().split()] for _ in range(N)]

    # print(A_list)
    T = [[0 for _ in range(7)] for _ in range(N)]

    # bfs
    def bfs(root):
        import collections

        que = collections.deque([[0, 0, -1]])
        while len(que)>0:
            temp = que.popleft()
            temp_node = temp[0]
            temp_depth = temp[1]
            temp_parent = temp[2]
            T[temp_node][0] = temp_node
            T[temp_node][1] = temp_parent 
            T[temp_node][4] = temp_depth
            print(temp)
            children = A_list[temp_node][1:2]
            cnt = 0
            for child in children:
                if child >= 0:
                    cnt +=1
                    que.append([[child, temp_depth+1, temp_parent]])
            T[temp_node][3] = cnt

            siblings = A_list[temp_parent][1:2]
            for sibling in siblings:
                if sibling != temp_node:
                    T[temp_node][2] = sibling


    for node, left, right in A_list:

        if T[node][1] == -1:
            T[node][6] = 'root' #type
        elif left == -1 and right == -1:
            T[node][6] = 'leaf'
        else:
            T[node][6] = 'internal node'

    bfs(0)
    print(T)
    
if __name__ == "__main__":
    resolve()
