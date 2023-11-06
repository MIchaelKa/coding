
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def items(self):            
        head = self    
        while head != None:
            yield head.val
            head = head.next

    def __iter__(self):
        return self.items()

def create_list_from_array(array: List) -> Optional[ListNode]:
    if len(array) == 0:
        return None
    head = ListNode(val=array[0])
    pos = head
    for i in range(1, len(array)):
        pos.next = ListNode(val=array[i])
        pos = pos.next
    return head
