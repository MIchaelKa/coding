"""
_0091_decode_ways

#dp

"""

class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 0 if s[-1] == "0" else 1

        for i in range(1, len(s)):

            prev_2 = s[len(s)-i+1] if i > 1 else "-1"
            prev_1 = s[len(s)-i]
            curr = s[len(s)-i-1]

            # print(curr, prev_1, prev_2)

            if curr == "0":
                dp[i+1] = 0                
            elif int(curr+prev_1) < 27:
                if  prev_2 != "0" and prev_1 != "0":
                    dp[i+1] = dp[i] + dp[i-1]
                elif prev_1 == "0": # and prev_2 != "0" 
                    dp[i+1] = dp[i-1]
                else:
                    dp[i+1] = dp[i]
            else:
                dp[i+1] = dp[i]

            # print(dp)

        return dp[-1]

def run_tests(solution):

    assert(solution.numDecodings("1221") == 5)
    assert(solution.numDecodings("11106") == 2)
    assert(solution.numDecodings("110211") == 3)
    assert(solution.numDecodings("06") == 0)
    assert(solution.numDecodings("0") == 0)
    assert(solution.numDecodings("230") == 0)
    assert(solution.numDecodings("27") == 1)
    assert(solution.numDecodings("99") == 1)

    print("tests passed!")


def main():
    solution = Solution()

    run_tests(solution)

    s = "1001"

    result = solution.numDecodings(s)
    print(result)