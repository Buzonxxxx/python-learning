# Functions
    # list()
    # print()
    # max()
    # min()
    # input()

# Methods
    # 'hello'.capitalize()

def super_func(name, *args, i='hi', **kwargs):
    """
    這個函數計算傳入的參數的總和。

    參數：
    name (str)：名字
    *args:位置參數
    i (str, optional)：預設值為 'hi' 的參數
    **kwargs:關鍵字參數

    返回值：
    int:傳入參數的總和
    """
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total
print(super_func('Louis', 1,2,3,4,5, num1=5, num2=10)) # 30

# exercise
def highest_even(li):
    evens = []
    for num in li:
        if num % 2 == 0:
            evens.append(num)
    return max(evens)
print(highest_even([10,2,3,4,8,11])) # 10

# walrus operator 這個運算子的符號是「:=」，它可以同時執行賦值和比較操作
a = 'helloooooooooo'
# n = len(a)
if (n := len(a)) > 10:
    print(f'too long {n} elements') # too long 14 elements

while (n := len(a)) > 1:
    print(n)
    a = a[:-1]
print(a)

# scope
total = 0

def count():
    global total
    total += 1
    return total

count()
count()
print(count()) # 3



