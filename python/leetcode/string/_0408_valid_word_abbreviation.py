"""
_0408_valid_word_abbreviation

Takeaways:

TODO:

Related problems:
Tags:

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O()
            memory: O()
    """
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        wp = 0
        ap = 0

        digit_str = None

        while wp < len(word) and ap < len(abbr):

            print(wp, ap, digit_str)

            if digit_str:
                if abbr[ap].isdigit():
                    digit_str += abbr[ap]
                    ap += 1
                else:
                    wp += int(digit_str)
                    digit_str = None
            elif word[wp] == abbr[ap]:
                wp += 1
                ap += 1
            elif abbr[ap].isdigit() and int(abbr[ap]):
                digit_str = abbr[ap]
                ap += 1
            else:
                return False

        if digit_str:
            wp += int(digit_str)

        return wp == len(word) and ap == len(abbr)

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    word = "internationalization"
    abbr = "i5a11o1"

    word = "a"
    abbr = "01"

    print(word, abbr)
    result = solution.validWordAbbreviation(word, abbr)
    print(result)


if __name__ == '__main__':
    main()