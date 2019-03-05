import random
class BinaryTree:
    def __init__(self, node=None):
        self.root = node
    def setRootNode(self, node):
        self.root = node
    def getRootNode(self):
        return self.root

# Need to decide what attributes the node object should have
class Node:
    # Idk if parsing in the parent node is necessary
    def __init__(self, arr: list, leftChild=None, rightChild=None, parent=None):
        self.array = arr
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parentNode = parent

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

    def split(self):
        h, w = len(self.array)-1, len(self.array[0])-1
        r = random.randint(0, 1)
        #Split vertically
        if r == 0:
            splitindex = random.randint(boundary_size, h - boundary_size)
            left, right = [], []
            for y in range(len(self.array)):
                left.append(self.array[y][:splitindex])
                right.append(self.array[y][splitindex:])
            print(len(self.array), len(left[0]), len(right[0]))
        else:
            v = random.randint(0, w)

def generate(w: int, h: int, min_size: int = 5) -> list:
    global boundary_size
    boundary_size = min_size
    arr = [[None for i in range(w)] for j in range(h)]
    Root = Node(arr)
    Tree = BinaryTree(Root)
    Tree.getRootNode().split()

generate(20, 20)