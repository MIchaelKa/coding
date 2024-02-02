'''
424. Longest Repeating Character Replacement

_0424_longest_repeat_char_replace


Notes:
Using heap can help?
heap + hash_map search

I didn't use the fact that only english uppercase letter is possible.
O(26) for search in counter

Links:
_0003_lswrc

Tags:
#array, #sliding_window

'''

class Solution_1:
    """
        Solution 1.

        Notes:
        It should take ~10 lines of codes
    """

    def characterReplacement(self, s: str, k: int) -> int:

        counter = {}
        start = 0

        max_len = 1

        max_char = s[0]
        max_count = 1 # maxf - we don't have to update it if it decrease

        for i in range(1, len(s)):

            # print(f'c={s[i]}, max_len={max_len}')

            if s[i] == max_char:
                max_count += 1
                max_len = max(max_len, i-start+1)
                continue

            counter[s[i]] = counter.get(s[i], 0) + 1

            # print(f'counter={counter}')

            if counter[s[i]] > max_count:
                counter[max_char] = max_count
                max_char = s[i]
                max_count = counter[s[i]]
                counter.pop(max_char)

            cur_edits = sum(counter.values())     

            while cur_edits > k:
                if s[start] == max_char:
                    max_count -= 1

                    # Find current maximum in counter
                    # max(counter.values())
                    max_edit_char = None
                    max_edit_count = 0
                    for c,v in counter.items():
                        if v > max_edit_count:
                            max_edit_char = c
                            max_edit_count = v

                    # Check if we should update external max
                    # TODO: dup code
                    if max_edit_count > max_count:
                        counter[max_char] = max_count
                        max_char = max_edit_char
                        max_count = max_edit_count
                        counter.pop(max_char)
                else:
                    counter[s[start]] -= 1
                    if counter[s[start]] == 0:
                        counter.pop(s[start])
                start += 1
                cur_edits = sum(counter.values())

            max_len = max(max_len, i-start+1)
 
        return max_len


class Solution:
    """
        Solution 2. Improved readability.

        Complexity:
            time: O(n*26)
            memory: O(26)
    """
    def characterReplacement(self, s: str, k: int) -> int:

        low = 0
        counter = {}
        counter[s[low]] = 1

        max_len = 1

        for high in range(1, len(s)):

            counter[s[high]] = counter.get(s[high], 0) + 1

            # TODO: remove while, keep max_freq
            while high-low+1 - max(counter.values()) > k:
                counter[s[low]] -= 1
                low += 1

            max_len = max(max_len, high-low+1)

        return max_len



def run_tests(solution):

    s = "ABBDBBA"
    k = 1
    answer = solution.characterReplacement(s, k)
    assert(answer==5)

    s = "AABABBA"
    k = 1
    answer = solution.characterReplacement(s, k)
    assert(answer==4)

    s = "BAAA"
    k = 0
    answer = solution.characterReplacement(s, k)
    assert(answer==3)

    print("test passed")


def main():
    solution = Solution()

    run_tests(solution)

    s = "ABBDBBA"
    k = 1

    print(s, k)
    answer = solution.characterReplacement(s, k)  
    print(answer)