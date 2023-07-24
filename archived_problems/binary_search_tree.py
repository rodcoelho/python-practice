class TreeNode:
    def __init__(self, value):
        # initialization of a node with value, and left and right children
        self.value = value
        self.lChild = None
        self.rChild = None

class Tree:
    def __init__(self):
        # initialize the root, this is our starting point in the tree
        self.root = None

    def makeRoot(self, value):
        # this allows for the creation of a Node
        self.root = TreeNode(value)

    def insert(self, value):
        # if no root exists then create one
        if (self.root is None):
            self.makeRoot(value)
        # otherwise insert a new node into the already existing tree
        else:
            self.insertNode(self.root, value)

    def insertNode(self, presentNode, value):
        # if new node value is less than present node, insert left
        if value <= presentNode.value:
            # if left child exists, then make left child present node and insert below it
            if presentNode.lChild:
                self.insertNode(presentNode.lChild, value)
            else:
                # if left child doesn't exist, make the value the left child
                presentNode.lChild = TreeNode(value)
        # if new node value is greater than the present node, insert right
        elif value > presentNode.value:
            # if right child exists, then make right child present node and insert below it
            if presentNode.rChild:
                self.insertNode(presentNode.rChild, value)
            else:
                # if right child doesn't exist, make the value the right child
                presentNode.rChild = TreeNode(value)

    def search(self, value):
        # calls SearchNode that recursively searches for value
        return self.searchNode(self.root, value)

    def searchNode(self, presentNode, value):
        # present node they are checking does not exist, then value does not exist in tree
        if presentNode is None:
            return False
        # if value is the same as the present node's value, then value exists in tree
        elif value == presentNode.value:
            return True
        # else if value is less than the current node, check left child
        elif value < presentNode.value:
            return self.searchNode(presentNode.lChild, value)
        # last option, check right
        else:
            return self.searchNode(presentNode.rChild, value)

    # this will traverse the tree and print every node's value
    def preorder(self):
        if self.root is not None:
            self.getnodes(self.root)
    # prints current node, then checks all left childs, then all right childs
    def getnodes(self, presentNode):
        print(presentNode.value)
        if presentNode.lChild is not None:
            return self.getnodes(presentNode.lChild)
        if presentNode.rChild is not None:
            return self.getnodes(presentNode.rChild)

    # function that prints every node's value in order from lowest to highest
    def inorder(self):
        if self.root is not None:
            self.ordergetnodes(self.root)
    # checks left, once at leaf, prints present node, then checks right
    def ordergetnodes(self, presentNode):
        if presentNode.lChild is not None:
            return self.getnodes(presentNode.lChild)
        print(presentNode.value)
        if presentNode.rChild is not None:
            return self.getnodes(presentNode.rChild)