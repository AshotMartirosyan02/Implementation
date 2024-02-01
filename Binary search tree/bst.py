from bts_node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val, node=None):
        if self.root is None:
            self.root = Node(val)
            return
        if node is None:
            node = self.root
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self.insert(val, node.left)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self.insert(val, node.right)

    def find(self, val, node=None):
        if node is None:
            if self.root is None:
                return "Not found"
            node = self.root

        if val == node.val:
            return "Found this number"
        elif val < node.val:
            if node.left is None:
                return "Not found"
            else:
                return self.find(val, node.left)
        else:
            if node.right is None:
                return "Not found"
            else:
                return self.find(val, node.right)

    def delete(self, val):
        self.root = self.__deleter(self.root, val)

    def __deleter(self, node, val):
        if node is None:
            return node
        if val < node.val:
            node.left = self.__deleter(node.left, val)
        elif val > node.val:
            node.right = self.__deleter(node.right, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.val = self.__poqri_node(node.right).val
            node.right = self.__deleter(node.right, node.val)
        return node

    def __poqri_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def height(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        left_height = self.height(node.left) if node.left is not None else 0
        right_height = self.height(node.right) if node.right is not None else 0
        return max(left_height, right_height) + 1



    def in_order(self, node=None):
        if node is None:
            node = self.root
        if node:
            if node.left:
                self.in_order(node.left)
            print(node.val, end=' ')
            if node.right:
                self.in_order(node.right)

    def pre_order(self, node=None):
        if node is None:
            node = self.root
        if node:
            print(node.val, end=' ')
            if node.left:
                self.pre_order(node.left)
            if node.right:
                self.pre_order(node.right)


    def post_order(self, node=None):
        if node is None:
            node = self.root
        if node:
            if node.left:
                self.post_order(node.left)
            if node.right:
                self.post_order(node.right)
            print(node.val, end=' ')





