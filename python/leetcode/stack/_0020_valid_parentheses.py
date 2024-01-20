'''
[leetcode] _0020_valid_parentheses

Related problems:
[skiena] _03_01_valid_parentheses

Tags:
#stack, #string

'''

class Solution:
    def isValid(self, s: str) -> bool:
        counters = []

        cur_open_char = ''
        cur_closed_char = ''

        char_dict = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        for c in s:
            if c == cur_open_char:
                counters[-1][1] += 1
            elif c == cur_closed_char:
                counters[-1][1] -= 1
            else:
                if c not in char_dict:
                    return False
                
                if len(counters) == 0:
                    counters.append([c, 1])
                else:
                    if counters[-1][1] == 0:
                        counters.pop()
                        if  len(counters) == 0:
                            counters.append([c, 1])
                        else:
                            if counters[-1][0] == cur_open_char:
                                counters[-1][1] += 1
                            else:
                                counters.append([c, 1])
                    else:
                        counters.append([c, 1])
                
                    
                cur_open_char = c
                cur_closed_char = char_dict[c]
                
            if counters[-1][1] < 0:
                return False
            
            if counters[-1][1] == 0:
                counters.pop()
                if  len(counters) != 0:
                    cur_open_char = counters[-1][0]
                    cur_closed_char = char_dict[cur_open_char]
                else:
                    cur_open_char = ''
                    cur_closed_char = ''
            
        for c in counters:
            if c[1] > 0:
                return False

        return True
    
class Solution_2:
    """
    Solution 2.
    Using stack.
    """
    def isValid(self, s: str) -> bool:

        stack = [None]

        char_dict = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for char in s:
            last_char = stack[-1]
            if char in char_dict and last_char == char_dict[char]:
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 1
    
def run_tests(solution):
    assert(solution.isValid("()[]{}")==True)
    assert(solution.isValid("()([}){}")==False)
    assert(solution.isValid("{[]}")==True)
    assert(solution.isValid("((((([[[[[")==False)

    print("Tests passed!")

    
def main():
    solution = Solution_2()

    run_tests(solution)

    # string = "{[]}"
    # string = "()[]{}"
    string = "()([}){}"

    answer = solution.isValid(string)
    print(answer)