from BooksModule import Book


class TreeNode:

    def __init__(self, book, left=None, right=None):
        self.book = book
        # self.book_info = BooksModule.Book.__repr__(book_info)
        self.leftChild = left
        self.rightChild = right

    # set a "current node". at the start this is the main parent node.
    # inspect the value at current node
    # if found, return the value
    # if the value we want is < the current node, go left
    # if the value we want is > the current node, go right
    # repeat the above steps until the searched value is found or until the bottom of the tree is reached.

    def search(self, searchBook, node):
        if node is None or node.book == searchBook:
            return node
        elif searchBook < node.book:
            return self.search(searchBook, node.leftChild)
        else: # searchValue > node.book:
            return self.search(searchBook, node.rightChild)

    def insert(self, newBook, node):
        if newBook < node.book:
            if node.leftChild is None:
                node.leftChild = TreeNode(newBook)
            else:
                self.insert(newBook, node.leftChild)
        elif newBook > node.book:
            if node.rightChild is None:
                node.rightChild = TreeNode(newBook)
            else:
                self.insert(newBook, node.rightChild)

    def delete(self, bookToDelete, node):
        # Base case: the parent has no children
        if node is None:
            return None
        # If the value we're deleting is < or > the current node, we set the L/R child respectively
        # to be the return value of a recursive call of this method on the current node's L/R subtree.
        elif bookToDelete < node:
            node.leftChild = self.delete(bookToDelete, node.leftChild)
            return node
        elif bookToDelete > node:
            node.rightChild = self.delete(bookToDelete, node.rightChild)
            return node
        elif bookToDelete == node.book:
            if node.leftChild is None:
                return node.rightChild
            elif node.rightChild is None:
                return node.leftChild
            else:
                node.rightChild = self.lift(node.rightChild, node)
            return node

    def lift(self, node, nodeToDelete):
        # If the current node in this fn has a left child, we recursively call this fn to
        # continue down the left subtree to find the successor node.
        if node.leftChild:
            node.leftChild = self.lift(node.leftChild, nodeToDelete)
            return node
        # If the current node has no left child, that means the current node of this fn is the successor node
        # and we take its value & make it the new value of the node that we're deleting:
        else:
            nodeToDelete.book = node.book
            # Return the successor node's right child to now be used as its parent's left child:
            return node.rightChild
