'''
424. Longest Repeating Character Replacement

_0424_longest_repeat_char_replace

...
Using heap can help?
heap + hash_map search

'''


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counter = {}
        start = 0

        max_len = 1

        max_char = s[0]
        max_count = 1

        for i in range(1, len(s)):

            print(f'c={s[i]}, max_len={max_len}')

            if s[i] == max_char:
                max_count += 1
                max_len = max(max_len, i-start+1)
                continue

            counter[s[i]] = counter.get(s[i], 0) + 1

            print(f'counter={counter}')

            if counter[s[i]] > max_count:
                counter[max_char] = max_count
                max_char = s[i]
                max_count = counter[s[i]]
                counter.pop(max_char)

            cur_edits = sum(counter.values())     

            while cur_edits > k:
                if s[start] == max_char:
                    max_count -= 1
                else:
                    counter[s[start]] -= 1
                    if counter[s[start]] == 0:
                        counter.pop(s[start])
                start += 1
                cur_edits = sum(counter.values())

            max_len = max(max_len, i-start+1)
 
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

    print("test passed")


def main():
    solution = Solution()

    # run_tests(solution)

    s = "BAAA"
    k = 0

    print(s, k)
    answer = solution.characterReplacement(s, k)  
    print(answer)