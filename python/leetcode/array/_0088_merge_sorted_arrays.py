"""
_0088_merge_sorted_arrays

Takeaways:

Related problems:

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O(n+m)
            memory: O(1)
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m-1
        j = n-1
        k = m+n-1

        while k >= 0:
            if i >= 0 and j >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            elif j >= 0:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
            



def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    nums1 = [0]
    m = 0
    nums2 = [2]
    n = 1

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [12,15,16]
    n = 3

    print(nums1, nums2)
    solution.merge(nums1, m, nums2, n)
    print(nums1)