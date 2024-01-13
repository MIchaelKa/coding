"""
[leetcode] 10. Regular Expression Matching

#dp

"""

def print_dp_matrix(s: str, p: str, matrix: list[list[int]]) -> None:
    print("[    ", end="")
    for i in range(len(s)):
        print(f"  {s[i]}", end="")
    print("]")

    for i in range(len(matrix)):
        print("[", end="")
        for j in range(len(matrix[i])+1):
            if j == 0 and i > 0:
                print(f"{p[i-1]}", end="")
            elif j == 0:
                print(" ", end="")
            else:
                print(f"{matrix[i][j-1]:3d}", end="")
        print("]")

class Solution:
    """
    Solution 1. Naive approach, does not work for all cases.
    """
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
    
class Solution2:
    """
    Solution 2. DP - Bottom-Up
    """
    def isMatch(self, s: str, p: str) -> bool:

        dp_matrix = [[False]*(len(s)+1) for _ in range(len(p)+1)]
        dp_matrix[0][0] = True
        for i in range(len(p)):       
            if p[i] == '*':
                top_match = dp_matrix[i-1][0] if i > 0 else True
                dp_matrix[i+1][0] = top_match

        for i in range(0, len(p)):
            for j in range(0, len(s)):
                if p[i] == '*':
                    star_char = p[i-1]
                    if star_char==s[j] or star_char == '.':
                        top2_left = dp_matrix[i-1][j] if i > 0 else False
                        top_left = dp_matrix[i-1][j+1] if i > 0 else False
                        left = dp_matrix[i+1][j] 
                        dp_matrix[i+1][j+1] = top2_left or left or top_left
                    else:
                        top_left = dp_matrix[i-1][j+1] if i > 0 else False
                        dp_matrix[i+1][j+1] = top_left
                else:
                    dp_matrix[i+1][j+1] = dp_matrix[i][j] and (p[i]==s[j] or p[i] == '.')

        # print_dp_matrix(s, p, dp_matrix)
        
        return dp_matrix[-1][-1]

def run_tests(solution):
    s = 'aabbb'
    p = 'a*b*'
    assert(solution.isMatch(s, p))

    s = 'ab'
    p = '.*'
    assert(solution.isMatch(s, p))

    s = 'aaa'
    p = 'a*a'
    assert(solution.isMatch(s, p))

    s = 'aabbb'
    p = 'a*c*b*'
    assert(solution.isMatch(s, p))

    s = 'aabbb'
    p = 'a*c*b*d'
    assert(not solution.isMatch(s, p))

    s = 'mississippi'
    p = 'mis*is*ip*.'
    assert(solution.isMatch(s, p))

    s = 'mississippi'
    p = 'mis*is*p*.'
    assert(not solution.isMatch(s, p))

    s = 'a'
    p = 'ab*a'
    assert(not solution.isMatch(s, p))

    s = 'aasdfasdfasdfasdfas'
    p = 'aasdf.*asdf.*asdf.*asdf.*s'
    assert(solution.isMatch(s, p))

    print("test passed")


if __name__ == '__main__':

    solution = Solution2()
    run_tests(solution)
 
    s = 'aasdfasdfasdfasdfas'
    p = 'aasdf.*asdf.*asdf.*asdf.*s'
    result = solution.isMatch(s, p)
    print(result)

