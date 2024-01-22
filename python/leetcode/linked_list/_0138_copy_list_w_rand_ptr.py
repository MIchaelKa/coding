"""
_0138_copy_list_w_rand_ptr

Takeaways:
- id(object) as a key for python dict

"""

from typing import List, Optional

class Node:
    def __init__(self, x: int = -1, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def items(self):            
        head = self    
        while head != None:
            yield (head.val, head.random.val if head.random else None )
            head = head.next

    def __iter__(self):
        return self.items()
    
    def __str__(self):
        return f"{self.val} - {self.random.val if self.random else None}"
    
    def __repr__(self):
        return f"{self.val} - {self.random.val if self.random else None}"


def create_list_from_array(array: List) -> Optional[Node]:

    head = None
    ptr = None
    items = [None] * len(array)

    for i in range(len(array)):

        if items[i] is None:
            items[i] = Node(array[i][0])
        else:
            items[i].val = array[i][0]
        
        if ptr is not None:
            ptr.next = items[i]
            ptr = items[i]
        else:
            head = items[i]
            ptr = items[i]

        if array[i][1] is not None:
            if items[array[i][1]] is None:
                items[array[i][1]] = Node()          
            items[i].random = items[array[i][1]]

    return head


class Solution:
    """
        Solution.

        Complexity:
            time: O(n)
            memory: O(n)
    """
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:

        new_head = None
        ptr = None
        items = {}

        while head != None:

            if id(head) not in items:
                items[id(head)] = Node(head.val)

            if ptr is not None:
                ptr.next = items[id(head)]
            else:
                new_head = items[id(head)]

            ptr = items[id(head)]

            if head.random is not None:
                if id(head.random) not in items:
                    items[id(head.random)] = Node(head.random.val)
                ptr.random = items[id(head.random)]

            head = head.next

        return new_head

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    array = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    head = create_list_from_array(array)
    print(list(head))

    result = solution.copyRandomList(head)
    print(list(result))