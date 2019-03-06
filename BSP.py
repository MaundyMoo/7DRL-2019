import random
class BinaryTree:
    def __init__(self, node=None):
        self.root = node
    def setRootNode(self, node):
        self.root = node
    def getRootNode(self):
        return self.root

    def postOrderTraversal(self, root, returnList: list = []):
        if root:
            self.postOrderTraversal(root.getleftChild())
            self.postOrderTraversal(root.getrightChild())
            returnList.append(root)
        return returnList

# Need to decide what attributes the node object should have
class Node:
    # Idk if parsing in the parent node is necessary
    def __init__(self, arr: list, leftChild=None, rightChild=None, parent=None):
        self.array = arr
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parentNode = parent
    '''
    def __repr__(self):
        _str = ""
        for each in self.array:
            _str += (str(each) + '\n').rstrip(' ')
        return _str
    '''
    def setleftChild(self, node):
        self.leftChild = node

    def setrightChild(self, node):
        self.rightChild = node

    def setParent(self, node):
        self.parentNode = node

    def getleftChild(self):
        try:
            return self.leftChild
        except AttributeError:
            return None

    def getrightChild(self):
        try:
            return self.rightChild
        except AttributeError:
            return None

    def getParent(self):
        return self.parentNode

    def returnChildren(self) -> tuple:
        return (self.leftChild, self.rightChild)

    def split(self):
        h, w = len(self.array)-1, len(self.array[0])-1
        r = random.randint(0, 1)
        #Split vertically
        if r == 0 and h > 2*boundary_size:
            print('vertical')
            splitindex = random.randint(boundary_size, h - boundary_size)
            left, right = [], []
            if len(self.array[0]) > boundary_size:
                for y in range(len(self.array)):
                    left.append(self.array[y][:splitindex])
                    right.append(self.array[y][splitindex:])
                self.setleftChild(Node(left))
                self.setrightChild(Node(right))
        elif w > 2*boundary_size:
            print('horizontal')
            splitindex = random.randint(boundary_size, w - boundary_size)
            if len(self.array) > boundary_size:
                v = random.randint(0, w)
                top = self.array[:splitindex]
                bottom = self.array[splitindex:]
                self.setleftChild(Node(top))
                self.setrightChild(Node(bottom))

def generate(w: int, h: int, min_size: int = 5, iterations: int = 3) -> list:
    global boundary_size
    boundary_size = min_size
    arr = [[None for i in range(w)] for j in range(h)]
    Root = Node(arr)
    Tree = BinaryTree(Root)
    iterate(Tree.getRootNode(), iterations)
    print(Tree.postOrderTraversal(Tree.getRootNode()))
    '''
    Tree.getRootNode().split()
    print(Tree.getRootNode(), '-' * 20 + '\n', Tree.getRootNode().getleftChild(), '-' * 20 + '\n', Tree.getRootNode().getrightChild(), end='', sep='')
    print(Tree.postOrderTraversal(Tree.getRootNode()))
    '''

def iterate(node, maxiters: int, iter: int = 0):
    if not iter == maxiters and not node is None:
        iter += 1
        node.split()
        iterate(node.getleftChild(), maxiters, iter)
        iterate(node.getrightChild(), maxiters, iter)

generate(20, 20)