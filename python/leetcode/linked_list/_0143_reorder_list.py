'''
143. Reorder List

_0143_reorder_list

Tags:
#linked_list

'''

from common.single_list import *

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head
        prev = None

        #TODO: remove need for is_even variable
        # stop slow pointer one node earlier in case of odd len
        is_even = True

        while fast is not None:

            fast = fast.next
            if fast is not None:
                fast = fast.next
            else:
                is_even = False
            
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        # print(list(prev))
        # print(list(slow))
        # print(is_even)

        if not is_even:
            fast = prev
            prev = prev.next
            fast.next = None


        while slow is not None:

            prev_next = prev.next
            slow_next = slow.next

            prev.next = slow     
            slow.next = fast

            fast = prev
            prev = prev_next
            slow = slow_next

        head = fast
      

def main():

    solution = Solution()

    # nums = [1,2,3,4,5,6,7,8]
    # nums = [1,2,3,4,5]
    nums = [1, 2, 3, 4, 5]
    head = create_list_from_array(nums)
    print(list(head))

    solution.reorderList(head)
    print(list(head))