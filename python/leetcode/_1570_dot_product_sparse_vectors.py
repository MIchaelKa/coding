"""
_1570_dot_product_sparse_vectors
https://leetcode.com/problems/dot-product-of-two-sparse-vectors

Takeaways:

TODO:

Related problems:
Tags:

"""

from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.map = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.map[i] = n
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:

        indexes = self.map.keys() & vec.map.keys()

        product = 0
        for i in indexes:
            product += self.map[i] * vec.map[i]

        return product

def main():

    nums1 = [1,0,0,2,3]
    nums2 = [0,3,0,4,0]

    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    
    print(nums1)
    print(nums2)
    ans = v1.dotProduct(v2)
    print(ans)


if __name__ == '__main__':
    main()