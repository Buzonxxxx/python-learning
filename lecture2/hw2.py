# -*- coding: utf-8 -*-

# 分別用for，while迴圈各寫⼀個nxn的乘法表 程式
# 可以讀取使用者輸入的值 n, n>1

# for
n = int(input("請輸入大於1的整數:"))
i = 0
j = 0

for i in range(1, n + 1):
  for j in range(1, n + 1):
    print(i, "*", j, "=", i * j)

# while
n = int(input("請輸入大於1的整數:"))
i = 1
j = 1

while i < n+1:
  while j < n+1:
    print(i, "*", j, "=", i * j)
    j += 1
  i += 1
  j = 1
