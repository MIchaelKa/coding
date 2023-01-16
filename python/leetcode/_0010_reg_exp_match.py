"""
[leetcode] 10. Regular Expression Matching
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        i = 0
        j = 0

        while i < len(s) and j < len(p):

            match_multiple = p[j+1] == '*' if j+1 < len(p) else False

            # print(f'{i}-{j}-{match_multiple}')

            if match_multiple:
                if p[j] == '.':
                    i = len(s)
                elif s[i] == p[j]:
                    i += 1
                    while i < len(s) and s[i] == s[i-1]:
                        i += 1
                j += 2
            elif s[i] == p[j] or p[j] == '.':
                i += 1
                j += 1
            else:
                return False
 

        return i == len(s) and j == len(p)

def run_tests():
    solution = Solution()
    s = 'aabbb'
    p = 'a*b*'
    assert(solution.isMatch(s, p))

    solution = Solution()
    s = 'ab'
    p = '.*'
    assert(solution.isMatch(s, p))

    print("test passed")


if __name__ == '__main__':
    run_tests()

    solution = Solution()
    s = 'aaa'
    p = 'a*a'
    result = solution.isMatch(s, p)
    print(result)

