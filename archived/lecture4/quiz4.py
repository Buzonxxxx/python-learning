# 將 for 迴圈範例 EX02_05.py 改寫成函式的寫法。
# 觀察涵式的回傳值
# 改寫成具有回傳值的版本
# 必定先定義而後呼叫

n = int(input('Please input n:'))

def sum_numbers(number):
    total = 0
    for i in range(1, number+1):
        total += i
    return total

print(sum_numbers(n))
