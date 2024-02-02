from bst import BinarySearchTree
from bst_node import Node

if __name__ == "__main__":
    node = Node(5)
    bst = BinarySearchTree(node)
    ls = [1,4,50,10,21]
    for i in ls:
        bst.insert(i)
    print(bst.height())
    bst.delete(10)
    bst.delete(44)
    print(bst.height())
    print(bst.find(1))
    print(bst.find(44))
    print("In order", end=" ")
    bst.in_order()
    print()
    print("Post order", end=" ")
    bst.post_order()
    print()
    print("Pre order", end=" ")
    bst.pre_order()

