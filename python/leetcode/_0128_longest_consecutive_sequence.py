'''
[leetcode] 128. Longest Consecutive Sequence

_0128_longest_consecutive_sequence

Tags:
#array

'''

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # (start, end) -> len
        # num -> (len, num)

        counter = {}

        for n in nums:

            if n-1 in counter and n+1 in counter:
                left = counter.pop(n-1)
                right = counter.pop(n+1)

                new_len = left[0] + right[0] + 1

                if left[1] is not None and right[1] is not None:
                    counter[left[1]] = (new_len, right[1])
                    counter[right[1]] = (new_len, left[1])
                elif left[1] is not None:
                    counter[left[1]] = (new_len, n+1)
                    counter[n+1] = (new_len, left[1])
                elif right[1] is not None:
                    counter[n-1] = (new_len, right[1])
                    counter[right[1]] = (new_len, n-1)
                else:
                    counter[n-1] = (new_len, n+1)
                    counter[n+1] = (new_len, n-1)

            elif n-1 in counter:
                item = counter.pop(n-1)
                new_len = item[0] + 1
                item_key = item[1]

                if item_key is None:
                    item_key = n-1
                
                counter[item_key] = (new_len, n)
                counter[n] = (new_len, item_key)
            elif n+1 in counter:
                item = counter.pop(n+1)
                new_len = item[0] + 1
                item_key = item[1]

                if item_key is None:
                    item_key = n+1
                
                counter[item_key] = (new_len, n)
                counter[n] = (new_len, item_key)
            elif n not in counter:
                counter[n] = (1, None)

            print(counter)

        print(counter)
        max = 0
        for k, v in counter.items():
            if v[0] > max:
                max = v[0]

        return max


if __name__ == '__main__':

    solution = Solution()

    # nums = [100,4,200,1,3,2]
    # nums = [2,1,4,5,3]
    # nums = [2,1,4,5,3,100,7,15,12,25,9,32,8,10,11]
    nums = [1,2,0,1]

    answer = solution.longestConsecutive(nums)
    print(answer)