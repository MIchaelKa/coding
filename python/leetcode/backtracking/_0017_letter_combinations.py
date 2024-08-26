"""
_0017_letter_combinations

Takeaways:
- Complexity for backtracking

Tags:
#backtracking

"""

from typing import List

class Solution:
    """
        Solution.

        Complexity:
            time: O(4^N*N) # 4^N - different combinations, N - to build each combination
            memory: O(N) # N - recursion call stack
    """
    def letterCombinations(self, digits: str) -> List[str]:

        digit_to_letter = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"],
        }

        result = []

        if not digits:
            return result

        def dfs(current_str: str):
            if len(current_str) == len(digits):
                result.append(current_str)
                return

            digit = digits[len(current_str)]

            for l in digit_to_letter[digit]:
                dfs(current_str+l)

        dfs("")

        return result

def run_tests(solution):
    print("test passed!")

def main():

    solution = Solution()

    run_tests(solution)

    digits = "237"

    print(digits)
    result = solution.letterCombinations(digits)
    print(result)


if __name__ == '__main__':
    main()