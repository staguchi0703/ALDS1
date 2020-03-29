def resolve():
    '''
    code here
    '''
    N = int(input())
    queries = [input().split() for _ in range(N)]

    class Node():
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    class BinaryTree():
        def __init__(self):
            self.root = None
            self.is_found = False

        def insert(self, val):
            if self.root == None:
                self.root = Node(val)
                # print('insert to root', val)
            else:
                # print('insert', val)
                node = self.root
                is_search = True
                while is_search:
                    # print('try insert to ', node.val)
                    if val <= node.val:
                        if node.left:
                            node = node.left
                        else:
                            node.left = Node(val)
                            is_search = False
                    else:
                        if node.right:
                            node = node.right
                        else:
                            node.right = Node(val)
                            is_search = False


        def show_inorder(self, node):
            if node == None:
                return

            self.show_inorder(node.left)
            print('', node.val, end='')
            self.show_inorder(node.right)


        def show_preorder(self, node):
            if node == None:
                return

            print('', node.val, end='')
            self.show_preorder(node.left)
            self.show_preorder(node.right)
        
        def find(self, node, target):
            if node == None:
                return
            if node.val == target:    
                self.is_found = True
                return
            
            self.find(node.left, target)
            self.find(node.right, target)


    bt = BinaryTree()

    for query, *val in queries:
        if query == 'insert':
            value = int(val[0])
            bt.insert(value)
        elif query == 'find':
            value = int(val[0])
            bt.find(bt.root, value)
            print('yes') if bt.is_found else print('no')
            bt.is_found = False
        else:
            bt.show_inorder(bt.root)
            print('')
            bt.show_preorder(bt.root)
            print('')



if __name__ == "__main__":
    resolve()
