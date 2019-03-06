import random
class BinaryTree:
    def __init__(self, node=None):
        self.root = node
    def setRootNode(self, node):
        self.root = node
    def getRootNode(self):
        return self.root

    #performs an iterative
    def Traversal(self):
        nodes = [self.root]
        stack = [self.root]
        while not len(stack) == 0:
            currNode = stack[-1]
            if not currNode.getleftChild() is None and currNode.getleftChild() not in nodes:
                stack.append(currNode.getleftChild())
                nodes.append(currNode.getleftChild())
            elif not currNode.getrightChild() is None and currNode.getrightChild() not in nodes:
                stack.append(currNode.getrightChild())
                nodes.append(currNode.getrightChild())
            else:
                currNode = stack.pop()
        return nodes

    def getLeafNodes(self, node = 'root', returnList = []):
        if node is 'root': node = self.root
        if node:
            self.postOrderTraversal(node.getleftChild(), returnList)
            self.postOrderTraversal(node.getrightChild(),returnList)
            if node.getleftChild() is None and node.getrightChild() is None:
                returnList.append(node)
        return returnList

# Need to decide what attributes the node object should have
class Node:
    # Idk if parsing in the parent node is necessary
    def __init__(self, x: int, y: int, height: int, width: int, leftChild=None, rightChild=None, parent=None):
        self.x, self.y = x, y
        self.width, self.height = width, height
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
        #Already split for whatever reason, simply stop
        if not self.leftChild is None and not self.rightChild is None:
            return False
        #Determine in which direction to split and how much
        #If either width or height is 25% larger we split that one
        #Otherwise random

        #splitH for split horizontally, if false we do vertically so no need for second flag
        splitH = random.randint(0,1) == 1
        if self.width > self.height and self.width / self.height > 1.25:
            splitH = True
        elif self.width < self.height and self.width / self.height < 1.25:
            splitH = False

        #ternary based on whether splitting horizontally or vertically
        maxVal = (self.width if splitH else self.height) - boundary_size
        #Too small to split
        if maxVal < boundary_size:
            return False

        #Value to split at
        split = random.randint(boundary_size, maxVal)
        if splitH:
            left = Node(self.x, self.y, self.width, split)
            right = Node(self.x, self.y + split, self.width, self.height - split)
        else:
            left = Node(self.x, self.y, split, self.height)
            right = Node(self.x + split, self.y, self.width - split, self.height)
        self.setleftChild(left)
        self.setrightChild(right)
        '''
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
        '''

def generate(w: int, h: int, min_size: int = 5, iterations: int = 2) -> list:
    global boundary_size
    boundary_size = min_size
    arr = [[None for i in range(w)] for j in range(h)]
    Root = Node(x = 0, y = 0, width = len(arr[0]), height = len(arr))
    Root.split()
    Tree = BinaryTree(Root)
    iterate(Tree.getRootNode(), iterations)
    print(Tree.getRootNode())
    nodes = Tree.Traversal()
    print(nodes, '\n', len(nodes))
    '''
    Tree.getRootNode().split()
    print(Tree.getRootNode(), '-' * 20 + '\n', Tree.getRootNode().getleftChild()\
    , '-' * 20 + '\n', Tree.getRootNode().getrightChild(), end='', sep='')
    print(Tree.postOrderTraversal(Tree.getRootNode()))
    '''

def iterate(node, maxiters: int, iter: int = 0):
    if not iter == maxiters and not node is None:
        iter += 1
        node.split()
        iterate(node.getleftChild(), maxiters, iter)
        iterate(node.getrightChild(), maxiters, iter)

generate(50, 50)