#-*-coding:UTF-8 -*-
# 類別作業練習 EX05_hw.py
#
# 測試資料 http://140.112.31.82/wordpress/?p=216

# 試寫一個名為 Student 的類別
# 其中屬性包含:
#  name, gender, grades
# 函數包含:
#  avg: 回傳grades list的平均值
#  add(grade): 新增成績到grades list中
#  fcount: 回傳不及格(<60)的總數
#  分別將每個學生的成績平均、不及格的的數目印出
# 寫一個名為top的類別函數:
#  傳入值為多個學生物件 (使用不定個數)
#  將平均分數最高的學生回傳

class Student:
  def __init__(self, n, g):
      self.name = n
      self.gender = g
      self.grades = []
  
  def avg(self):
    avg = sum(self.grades) / len(self.grades)
    return avg

  def add(self, grade):
    self.grades.append(grade)  

  def fcount(self):
    self.failGrades = []
    for i in self.grades:
      if i < 60:
        failGrades.append(i)
    return len(failGrades)


a = Student("Louis", "M")
a.add(10)
print(a.grades)  
print(a.avg())  
print(a.fcount)


# s1 = student("Tom","M")
# s2 = student("Jane","F")
# s3 = student("John","M")
# s4 = student("Ann","F")
# s5 = student("Peter","M")
# s1.add(80)
# s1.add(90)
# s1.add(55)
# s1.add(77)
# s1.add(40)
# s2.add(58)
# s2.add(87)
# s3.add(100)
# s3.add(80)
# s4.add(40)
# s4.add(55)
# s5.add(60)
# s5.add(60)

