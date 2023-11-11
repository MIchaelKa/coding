'''
[leetcode] 128. Longest Consecutive Sequence

_0128_longest_consecutive_sequence

Tags:
#array

'''

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        counter = {}

        for n in nums:

            # print(n)

            if n-1 in counter and n+1 in counter:
                left = counter.pop(n-1)
                right = counter.pop(n+1)

                if left is not None and right is not None:
                    counter[left] = right
                    counter[right] = left
                elif left is not None and left < n:
                    counter[left] = n+1
                    counter[n+1] = left
                elif right is not None and right > n :
                    counter[n-1] = right
                    counter[right] = n-1
                elif left is None and right is None:
                    counter[n-1] = n+1
                    counter[n+1] = n-1

            elif n-1 in counter:
                left = counter[n-1]
                if left is None:
                    counter[n-1] = n
                    counter[n] = n-1
                elif left < n:
                    counter[left] = n
                    counter[n] = left
                    counter.pop(n-1)

            elif n+1 in counter:
                right = counter[n+1]
                if right is None:
                    counter[n+1] = n
                    counter[n] = n+1
                elif right > n:
                    counter[right] = n
                    counter[n] = right
                    counter.pop(n+1)
            elif n not in counter:
                counter[n] = None

            # print(f'{counter}, len: {len(counter)}')

        print(f'{counter}, len: {len(counter)}')

        max_len = 0
        for k, v in counter.items():
            if v is None:
                cur_len = 1
            else:
                max_elem, min_elem = k, v # if k > v else v, k
                cur_len = max_elem - min_elem + 1
                
            if cur_len > max_len:
                max_len = cur_len

        return max_len

def run_tests(solution):

    nums = [100,4,200,1,3,2]
    result = solution.longestConsecutive(nums)
    assert(result==4)

    nums = [2,1,4,3,100,7,15,12,25,9,32,8,10]
    result = solution.longestConsecutive(nums)
    assert(result==4)

    nums = [2,1,4,3,100,7,15,12,25,9,32,8,6,10,11]
    result = solution.longestConsecutive(nums)
    assert(result==7)

    nums = [-2,-3,-3,7,-3,0,5,0,-8,-4,-1,2]
    result = solution.longestConsecutive(nums)
    assert(result==5)

    nums = [-9,-4,9,-7,0,7,3,-1,6,2,-2,8,-2,0,2,-7,-5,-2,6,-5,0,-8,8,1,0,6,8,-8,-1]
    result = solution.longestConsecutive(nums)
    assert(result==6)

    print("Tests passed!")

if __name__ == '__main__':

    solution = Solution()

    run_tests(solution)

    nums = [-9,-4,9,-7,0,7,3,-1,6,2,-2,8,-2,0,2,-7,-5,-2,6,-5,0,-8,8,1,0,6,8,-8,-1]
    # nums = [-2,-1,0,1,2,3,-1]

    answer = solution.longestConsecutive(nums)
    print(answer)