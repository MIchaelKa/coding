from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def show(self):
        for i in self.items():
            print(i, end=" ")
        print("")
            
    def items(self):
        if self.left is not None:
            yield from self.left.items()
            
        yield self.val
        
        if self.right is not None:
            yield from self.right.items()

    def show_pre_order(self):
        for i in self.items_pre_order():
            print(i, end=" ")
        print("")

    def items_pre_order(self):
        yield self.val

        if self.left is not None:
            yield from self.left.items_pre_order()
        
        if self.right is not None:
            yield from self.right.items_pre_order()
            
    def __iter__(self):
        return self.items()

#
# Methods
#

def insert(head: TreeNode, val: int):
    if head.val == val:
        return # no dups
    
    if head.val < val:
        if head.right is None:
            head.right = TreeNode(val=val)
        else:
            insert(head.right, val)
    else:
        if head.left is None:
            head.left = TreeNode(val=val)
        else:
            insert(head.left, val)


def init_tree_from_array(array: list) -> Optional[TreeNode]:
    
    if len(array) == 0:
        return None
    
    head = TreeNode(val=array[0])
    
    for i in range(1, len(array)):
        insert(head, array[i])
        
    return head

def swap(first: TreeNode, second: TreeNode):
    buffer = first.val
    first.val = second.val
    second.val = buffer


if __name__ == '__main__':
    tree = init_tree_from_array([5,9,1,45,3,2,12,7,13])
    tree.show()
    tree.show_pre_order()
    