'''
_0020_valid_parentheses
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
    def isValid(self, s: str) -> bool:

        return True
    
def run_tests(solution):
    assert(solution.isValid("()[]{}")==True)
    assert(solution.isValid("()([}){}")==False)
    assert(solution.isValid("{[]}")==True)
    assert(solution.isValid("((((([[[[[")==False)

    print("Tests passed!")

    
def main():
    solution = Solution()

    run_tests(solution)

    answer = solution.isValid("{[]}")
    print(answer)