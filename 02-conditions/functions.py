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
    *args是用於接收任意數量的位置參數。當你不確定函數會接收多少個位置參數時,可以使用*args。
    在函數內部，*args會將傳入的位置參數打包成一個元組(tuple)，你可以通過迭代或索引來訪問這些參數。

    **kwargs是用於接收任意數量的關鍵字參數。類似於*args,**kwargs允許你在函數中接收不確定數量的關鍵字參數。
    在函數內部，**kwargs會將傳入的關鍵字參數打包成一個字典(dictionary),你可以通過鍵(key)來訪問這些參數的值。
    這個函數計算傳入的參數的總和。

    返回值：
    int:傳入參數的總和
    """
    print(args) # (1, 2, 3, 4, 5)
    print(kwargs) # {'num1': 5, 'num2': 10}
    total = 0
    for items in kwargs.values():
        total += items

    print(total) # 15
    print(args) # (1, 2, 3, 4, 5)
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
if (n := len(a)) > 10:
    print(f'too long {n} elements') # too long 14 elements

while (n := len(a)) > 1:
    print(n) # 14 13 12 11 10 9 8 7 6 5 4 3 2
    a = a[:-1]
print(a)

# scope
total = 0

def count():
    global total # 這個變數是全局變數
    total += 1
    return total

count()
count()
print(total) # 2



