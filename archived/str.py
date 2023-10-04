import random

##### 切片 #####

# string
# toast = "PYTHONSLICE"
# print(toast[-5])
# print(toast[-5:])
# print (toast[:5]+toast[5:])

# tuple
# n = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")[3]
# print(n)
# toast = "PYTHONSLICE"
# tuples=toast[0:3],toast[3:6],toast[6:9],toast[9:11]
# print(tuples)

# list
# n = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"][random.randint(0,6)]
# print(n)
# n = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
# n[2] = "星期二" # list可以取代值, tuple不可以
# print(n)

# dic
# days={
#   1:"Sunday",
#   2:"Monday",
#   3:"Tuesday",
#   4:"Wednesday",
#   5:"Thursday",
#   6:"Friday",
#   7:"Saturday"
#   }
# n = days[2],days[3],days[4]
# print(n)

# number
# n = 123456
# print(str(n)[0])

##### flag #####

# print("會員編號1:%d, 會員編號2:%d" % (10, 20))
# print("會員編號2:%(#2)d, 會員編號1:%(#1)d" % {"#1": 10, "#2": 20})
# print("會員編號1:%(num1)d, 會員編號2:%(num2)d" % {"num1": 10, "num2": 20})

# print("會員編號:%(#)08d" % {"#" : 123456})
# print("%8.2f" % (123.456))

# # %* passes all arguments
# money=987.98
# print("$%*.2f" % (7, money))

# print ('hello'.capitalize())

# text='abbggccdeefgggijklgglmo'
# print (text.count('g'))
# print (text.count('g',4,-4))

# images = "xbox.gif, iphone.jpg"
# print(images.endswith(".jpg"))
# print(images.endswith(".gif", 0, 8))
# print(images.endswith(".gif"))

# text = 'abcdefgabcdefg'
# print(text.find('x'))
# print(text.find('a', 1))
# print(text.find('a', 9))

# print("{0} makes a full man, and {1} an exact man.".format("Reading", "writing"))

# 與string.find()類似，差異在當s字串變數內搜尋不到sub字串, 會回傳ValueError錯誤訊息
# text = "abcdeabcde"
# print(text.index('d', 4))

# # 判斷該變數裡的內容是否為[a-z]、[A-Z]與[0-9]的字元
# print(str.isalnum('%'))
# # 是否英文字母
# print(str.isalpha('a'))
# # 是否整數
# print(str.isdigit('a'))
# # 是否都小寫
# print(str.islower('a'))
# # 是否空白字元
# print(str.isspace(' '))
# # 判斷字串變數裡的第⼀個字是否為⼤寫
# print(str.istitle('Hello'))
# # 判斷字串變數內的所有字⺟都必須要⼤寫, 不會理會特殊字元
# print(str.isupper('AA$$GD'))

# 返回字符串左對齊的字符串長度寬度。填充是通過使用指定的fillchar（默認為空格)
# str.ljust(width[, fillchar])
# width -- 這是填充後字符串的總長度。
# fillchar -- 這是填充符，默認為空格。
# text="abcdefghijkl"
# print(text.ljust(50, '0'))

# # 從⼤寫字⺟轉換為⼩寫字⺟
# print('Hello'.lower())
# print('Hello'.upper())

# # replace chars
# print('Hello'.replace('l', 'x', 1)) 

# # 從右到左尋找，sub引數是預計要搜尋的字元
# print('Hello'.rfind('e'))

# # 將s字串變數內左邊的多於空⽩字元去掉，chars引數必須傳⼊字串型態
# text = " aaaaa bbbbbbaaaccccc"
# print(text.lstrip())

# # 將字串做分割，但只會分割第⼀個符合sep引數的字元，形成3-tuple
# names = 'Tom,John,Mary,Bob,Sunny'
# print(names.partition(','))
# print(names.partition(',')[-1])
# print(names.rpartition(','))

# # string split
# print(names.split(','))

# # 將字串內所有為[a-z]的單字第⼀個字元轉換成⼤寫
# print('123hahahahah'.title())