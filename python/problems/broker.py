#
# see _0121_best_time_buy_sell.py
#

#
# Брокер
#
# Дан массив, в котором i-й элемент обозначает цену акции в i-й день торгов.
# Вам дано совершить только одну транзакцию: купить и только затем продать акцию.
# Найдите максимальную возможную прибыль такой транзакции.
# 
# Примеры:
# Input: [7,1,5,3,6,4]
# Output: 5
# 
# Input: [7,6,4,3,1]
# Output: 0
# Нет прибыли, ответ 0
# 

#
# Solution 1. Brute Force
#
def solution(x):
    len_x = len(x)
    max_t = 0

    for i in range(len_x):
        for j in range(i+1, len_x):
            t = x[j] - x[i]
            if t > max_t:
                max_t = t
                
    return max_t

#
# Solution 2. One Pass
#
def solution(x):
    len_x = len(x)
    min_t = 999 # int_max
    diff = 0

    for i in range(len_x):
        min_t = min(min_t, x[i])
        diff = max(diff, x[i] - min_t)
                
    return diff

x = [7,1,5,3,6,4]
solution(x)

if __name__ == '__main__':

    x = [7,1,5,3,6,4]
    result = solution(x)
    print(result)