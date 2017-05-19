import random
class Node:
    def __init__(self, key, dad=None, color=0):
        self.key = key
        self.left = None
        self.right = None
        self.dad = dad
        self.color = color

    def get(self):
        return self

    def set(self, key):
        self.key = key

    def getChildren(self):
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        return children

    def getdad(self):
        return self.dad


class ABR:
    def __init__(self):
        self.root = None

    def setRoot(self, key):
        self.root = Node(key)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key, None, 0)

        else:
            self.insertNode(Node(key, None, 0))

    def insertNode(self, currentNode):
        y = None
        x = self.root
        while x is not None:
            y = x
            if currentNode.key < y.key:
                x = x.left
            else:
                x = x.right
        currentNode.dad = y
        if y is None:
            self.root = currentNode
        elif currentNode.key < y.key:
            y.left = currentNode
        else:
            y.right = currentNode

    def find(self, key, color=0):
        return self.findNode(self.root, key, color)

    def findNode(self, currentNode, key, color):
        if currentNode is None:
            return False
        elif key == currentNode.key and color == currentNode.color:
            return True
        elif key < currentNode.key:
            return self.findNode(currentNode.left, key, color)
        else:
            return self.findNode(currentNode.right, key, color)

    def find_delete(self, key, color=0):
        return self.findNode_delete(self.root, key, color)

    def findNode_delete(self, currentNode, key, color):
        if currentNode is None:
            return False
        elif key == currentNode.key and color == currentNode.color:
            return currentNode
        elif key < currentNode.key:
            return self.findNode_delete(currentNode.left, key, color)
        else:
            return self.findNode_delete(currentNode.right, key, color)

    def inorder(self):
        def _inorder(v):
            if v is not None:
                _inorder(v.left)
                print v.key
                _inorder(v.right)
        _inorder(self.root)

    def height(self):
        def _height(v):
            if v is None:
                return -1
            else:
                alt_sx = _height(v.left)
                alt_dx = _height(v.right)
                return max(alt_sx, alt_dx) + 1
        return _height(self.root)

    def min(self):
        print "il valore minimo e': ", self._min(self.root)

    def _min(self, currentNode):
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.get()

    def max(self):
        print "il valore minimo e': ", self._max(self.root)

    def _max(self, currentNode):
        while currentNode.right is not None:
            currentNode = currentNode.right
        return currentNode.get()

    def transplant(self, u, v):
        if u.dad is None:
            self.root = v
        elif u is u.dad.left:
            u.dad.left = v
        else:
            u.dad.right = v
        if v is not None:
            v.dad = u.dad

    def delete(self, key):
        if self.root is None:
            print "lista vuota"
        else:
            currentNode = self.find_delete(key)
            if currentNode is False:
                return -1
            self._delete(currentNode)

    def _delete(self, currentNode):
        if currentNode.left is None:
            self.transplant(currentNode, currentNode.right)
        elif currentNode.right is None:
            self.transplant(currentNode, currentNode.left)
        else:
            y = self._min(currentNode.right)
            if y.dad is not currentNode:
                self.transplant(y, y.right)
                y.right = currentNode.right
                y.right.dad = y
            self.transplant(currentNode, y)
            y.left = currentNode.left
            y.left.dad = y


class ARN:
    def __init__(self):
        self.nil = Node(None)
        self.root = self.nil

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, self.nil, 0)
        else:
            self._insert(Node(data, self.nil, 0))

    def _insert(self, currentNode):
        y = self.nil
        x = self.root
        while x is not self.nil:
            y = x
            if currentNode.key < x.key:
                x = x.left
            else:
                x = x.right
        currentNode.dad = y
        if y is self.nil:
            self.root = currentNode
        elif currentNode.key < y.key:
            y.left = currentNode
        else:
            y.right = currentNode
        currentNode.left = self.nil
        currentNode.right = self.nil
        currentNode.color = 1
        self._insertFix(currentNode)

    def height(self):
        def _height(v):
            if v is self.nil:
                return -1
            else:
                alt_sx = _height(v.left)
                alt_dx = _height(v.right)
                return max(alt_sx, alt_dx) + 1
        return _height(self.root)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.nil:
            y.left.dad = x
        y.dad = x.dad
        if x.dad is self.nil:
            self.root = y
        elif x is x.dad.left:
            x.dad.left = y
        else:
            x.dad.right = y
        y.left = x
        x.dad = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right is not self.nil:
            x.right.dad = y
        x.dad = y.dad
        if y.dad is self.nil:
            self.root = x
        elif y is y.dad.right:
            y.dad.right = x
        else:
            y.dad.left = x
        x.right = y
        y.dad = x

    def _insertFix(self, currentNode):
        while currentNode.dad.color is 1:
            if currentNode.dad is currentNode.dad.dad.left:
                y = currentNode.dad.dad.right
                if y.color is 1:
                    currentNode.dad.color = 0
                    y.color = 0
                    currentNode.dad.dad.color = 1
                    currentNode = currentNode.dad.dad
                else:
                    if currentNode is currentNode.dad.right:
                        currentNode = currentNode.dad
                        self.left_rotate(currentNode)
                    currentNode.dad.color = 0
                    currentNode.dad.dad.color = 1
                    self.right_rotate(currentNode.dad.dad)
            else:
                y = currentNode.dad.dad.left
                if y.color is 1:
                    currentNode.dad.color = 0
                    y.color = 0
                    currentNode.dad.dad.color = 1
                    currentNode = currentNode.dad.dad
                else:
                    if currentNode is currentNode.dad.left:
                        currentNode = currentNode.dad
                        self.right_rotate(currentNode)
                    currentNode.dad.color = 0
                    currentNode.dad.dad.color = 1
                    self.left_rotate(currentNode.dad.dad)
        self.root.color = 0

    def find(self, key, color=0):
        return self.findNode(self.root, key, color)

    def findNode(self, currentNode, key, color):
        if currentNode is None:
            return False
        elif key == currentNode.key and color == currentNode.color:
            return True
        elif key < currentNode.key:
            return self.findNode(currentNode.left, key, color)
        else:
            return self.findNode(currentNode.right, key, color)


tree = ARN()
A = range(800)
for i in range(0, 800):
    tree.insert(A[i])
#tree.insert(5)
#print "L'altezza dell'albero e': ", tree.height()
#tree.insert(2)
#tree.insert(3)
#tree.insert(6)
print "L'altezza dell'albero e': ", tree.height()
#tree.inorder()
#print tree.find(5)
#print tree.find(2)
#print tree.find(3)
#tree.delete(5)
#tree.delete(3)
#tree.delete(6)
#tree.inorder()
