class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        time_digits = [time[0], time[1], time[3], time[4]]     
        time_digits = [int(d) for d in time_digits]
        
        def d2s(t) -> str:
            t = [str(td) for td in t]
            return ''.join([t[0], t[1], ":", t[2], t[3]])
        
        def best_digit(num, bound) -> int:
            digits = [d for d in time_digits if d > num and d <= bound]
            if digits:
                return min(digits)
            else:
                return -1
        
        res = best_digit(time_digits[3], 9)
        if res > 0:
            time_digits[3] = res
            return d2s(time_digits)
        
        res = best_digit(time_digits[2], 5)
        if res > 0:
            time_digits[2] = res
            return d2s(time_digits)
        
        if time_digits[0] < 2:
            res = best_digit(time_digits[1], 9)
            if res > 0:
                time_digits[1] = res
                return d2s(time_digits)
        else:     
            res = best_digit(time_digits[1], 3)
            if res > 0:
                time_digits[1] = res
                return d2s(time_digits)
                       
        res = best_digit(time_digits[0], 2)
        if res > 0:
            time_digits[0] = res
            return d2s(time_digits)
        
        min_d = min(time_digits)
        return d2s([min_d,min_d,min_d,min_d])


def main():

    solution = Solution()

    time = "13:55"

    print(time)
    result = solution.nextClosestTime(time)
    print(result)
        
if __name__ == '__main__':
    main()      
        
        
        
        
        
        