"""
_0328_odd_even_list

Takeaways:

"""

from common.single_list import *

class Solution:
    """
        Solution.

        Complexity:
            time: O(n)
            memory: O(1)
    """
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        even_head = head.next
        if even_head is None:
            return head
        
        odd_ptr = head
        even_ptr = even_head

        while odd_ptr.next and even_ptr.next:

            odd_ptr.next = even_ptr.next
            odd_ptr = odd_ptr.next

            if even_ptr.next.next:
                even_ptr.next = even_ptr.next.next
                even_ptr = even_ptr.next
            else:
                even_ptr.next = None
        
        odd_ptr.next = even_head

        return head


def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums = [1, 2, 3, 4, 5, 6, 7]
    nums = [2]
    head = create_list_from_array(nums)
    print(list(head))

    result = solution.oddEvenList(head)
    print(list(result))