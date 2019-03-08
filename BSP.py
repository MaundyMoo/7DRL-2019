import random
class BinaryTree:
    def __init__(self, node=None):
        self.root = node
    def setRootNode(self, node):
        self.root = node
    def getRootNode(self):
        return self.root

    #performs an iterative approach to traversal
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
        nodes = self.Traversal()
        leafNodes = []
        for node in nodes:
            if node.getleftChild() is None and node.getrightChild() is None:
                leafNodes.append(node)
        return leafNodes

# Need to decide what attributes the node object should have
class Node:
    # Idk if parsing in the parent node is necessary
    def __init__(self, x: int, y: int, width: int, height: int, leftChild=None, rightChild=None, parent=None):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parentNode = parent

        self.room: tuple

    @property
    def values(self):
        return (self.x, self.y, self.width, self.height)

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
        if self.width > self.height and self.width / self.height >= 1.25:
            splitH = False
        elif self.height > self.width and self.height / self.width >= 1.25:
            splitH = True

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

    def createRooms(self):
        if not self.leftChild is None or not self.rightChild is None:
            if not self.leftChild is None:
                self.leftChild.createRooms()
            if not self.rightChild is None:
                self.rightChild.createRooms()
        else:
            roomSize: tuple
            roomPos: tuple
            #Min size is 3x3 and max within 1 of the leaf size
            roomSize = (random.randint(3, self.width - 1),
                        random.randint(3, self.height - 1))

            #Place the rooom within the room, but not touching the edge
            print(1, self.width - roomSize[0] - 1)
            roomPos = (random.randint(1, self.width - roomSize[0]),
                       random.randint(1, self.height - roomSize[1]))
            #(x, y, width, height)
            self.room = (self.x + roomPos[0], self.y + roomPos[1],
                         roomSize[0], roomSize[1])
def checkLeaves(arr, leaves):
    counter = 0
    for leaf in leaves:
        counter += 1
        #vals(x, y, width, height)
        print(leaf.values)
        (x, y, width, height) = leaf.room
        for i in range(y, y+height):
            for j in range(x, x+width):
                arr[i][j] = counter
    for each in arr:
        print(each)

def iterate(node, maxiters: int, iter: int = 0):
    if not iter == maxiters and not node is None:
        iter += 1
        node.split()
        iterate(node.getleftChild(), maxiters, iter)
        iterate(node.getrightChild(), maxiters, iter)

def generate(w: int, h: int, min_size: int = 5, iterations: int = 2) -> list:
    global boundary_size
    boundary_size = min_size
    arr = [[0 for i in range(w)] for j in range(h)]
    Root = Node(x = 0, y = 0, width = len(arr[0]), height = len(arr))
    Root.split()
    Tree = BinaryTree(Root)
    iterate(Tree.getRootNode(), iterations)
    nodes = Tree.Traversal()
    leaves = Tree.getLeafNodes()
    Tree.getRootNode().createRooms()
    checkLeaves(arr, leaves)

generate(20, 20)